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

def timesheet_check_interval():
    print("Hello from task!")
    # msg = EmailMessage()
    #
    # asparagus_cid = make_msgid()
    # msg.add_alternative("Test Message")
    # fromEmail = 'amir.behvandi@tescan.ca'
    # toEmail = "amirbehvandi747@gmail.com"
    #
    # msg['Subject'] = 'Timesheet interval tester.'
    # msg['From'] = fromEmail
    # msg['To'] = toEmail
    # # msg['Cc'] = 'customersupportdesk@tescan.ca'
    #
    # s = smtplib.SMTP('mail.tescan.ca', 26)
    # s.starttls()
    # s.login(fromEmail, 'Daj21372')
    # s.send_message(msg)
    # s.quit()
    # print("Email was sent!")



    rec_list = []
    user_list = User.objects.filter(groups__name__in=['Staff', 'training_admin', 'admin', 'training_operator'])
    for user in user_list:
        if Timesheet.objects.filter(staff=user).count() > 0:
            last_record = Timesheet.objects.select_related('staff').filter(staff=user).last()
            if last_record.from_temp < datetime.datetime.now() - timedelta(days=7):
                rec_list.append(last_record)
                print(last_record.staff.username + ' : ' + str(last_record.from_temp))

        # if item.diff.days > 10:
        #     candidate = TesCandidate.objects.filter(user=item.staff).first()
        #     print(candidate.first_name +': ' + str(item.diff.days) )
        #     timesheet = Timesheet.objects.first()
        #     obj = TimesheetChecker()
        #     obj.timesheet = timesheet
        #     obj.trigger = True
            # obj.save()