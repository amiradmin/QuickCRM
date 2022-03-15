import requests
from scheduler.models import TimesheetChecker
from email.message import EmailMessage
from email.utils import make_msgid
from stafftimesheet.models import Timesheet
from django.db.models import Q ,F
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


    # now = datetime.datetime.now()
    # timesheet_list = Timesheet.objects.annotate(diff=now - F('from_temp'))
    # for item in timesheet_list:
    #     # print(item)
    #     if item.diff > datetime.timedelta(days=7):
    #         print(item.staff.first_name +': ' + str(item.diff.seconds // 3600))
    #
    # timesheet = Timesheet.objects.first()
    # obj = TimesheetChecker()
    # obj.timesheet = timesheet
    # obj.trigger = True
    # obj.save()