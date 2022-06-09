import requests
from scheduler.models import TimesheetChecker
from email.message import EmailMessage
from email.utils import make_msgid
from stafftimesheet.models import Timesheet
from django.db.models import Q ,F,Count
from training.models import TesCandidate
from django.contrib.auth.models import User
from datetime import datetime,date, timedelta
import datetime
import smtplib
from celery import shared_task


@shared_task
def cerExpiration(x, y):
    print("Inside Task")
    return x + y


def timesheet_check_interval():
    print("Hello from task!")


    rec_list = []
    user_list = User.objects.filter(
        groups__name__in=['Staff', 'training_admin', 'admin', 'training_operator', 'management'])
    for user in user_list:
        can_count = TesCandidate.objects.filter(user=user).count()
        tes_task = TimesheetChecker()
        if can_count > 0:
            tesCandidate = TesCandidate.objects.filter(user=user).first()
            if tesCandidate.disable_timesheet == False:
                # print(user)
                if Timesheet.objects.filter(staff=user).count() > 0:
                    last_record = Timesheet.objects.select_related('staff').filter(staff=user).last()
                    if last_record.from_temp < datetime.datetime.now() - timedelta(days=7):
                        tesCandidate = TesCandidate.objects.filter(user=user).first()
                        rec_list.append(tesCandidate)

                        print(last_record.staff.username + ' : ' + str(last_record.from_temp))
                else:
                    tesCandidate = TesCandidate.objects.filter(user=user).first()
                    rec_list.append(tesCandidate)
                    # print("empty timesheet: "+ tesCandidate.email + ' = ' +str(Timesheet.objects.filter(staff=user).count()))

    for item in rec_list:
        print(item.email)

        tes_task.date = datetime.datetime.now() + timedelta(days=7)
        tes_task.save()
        print("Start mailing")
        msg = EmailMessage()

        asparagus_cid = make_msgid()
        msg.add_alternative("You haven’t completed your timesheet recently. Please make sure to submit it at your earliest time. Thank you.")
        fromEmail = 'erp@tescan.ca'
        toEmail = item.email

        msg['Subject'] = 'Timesheet Reminder.'
        msg['From'] = fromEmail
        msg['To'] = toEmail

        # msg['Cc'] = 'customersupportdesk@tescan.ca'

        s = smtplib.SMTP('smtp-mail.outlook.com', 25)
        s.starttls()
        s.login(fromEmail, 'Wuh28931')
        s.send_message(msg)
        s.quit()
        print("Email was sent!")