from django.shortcuts import render, redirect
from email.message import EmailMessage
from email.utils import make_msgid
from django.contrib.auth.models import User
import smtplib
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.contrib.auth.mixins import LoginRequiredMixin
from authorization.sidebarmixin import SidebarMixin
from django.views.generic import View, TemplateView
from training.models import TesCandidate
from sendgrid.helpers.mail import *
from dotenv import load_dotenv
from braces.views import GroupRequiredMixin
from django.db.models import Q
import sendgrid
import os
import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from mailchimp import Mailchimp
import pandas as pd
import json
from django.utils.html import strip_tags



class SingleMailSender(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "mailer/send_mail.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']

    def get_context_data(self, *args, **kwargs):
        context = super(SingleMailSender, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        candidate_list = TesCandidate.objects.all()
        context['candidate'] = candidate
        context['group_name'] = group_name
        context['candidate_list'] = candidate_list

        return context


    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            print('Single mail')
            project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            load_dotenv(os.path.join(project_folder, '.env'))
            MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')

            user_list = User.objects.filter(
                groups__name__in=['Staff', 'training_admin', 'admin', 'training_operator', 'management'])

            email_list = TesCandidate.objects.filter(Q(user__id__in=user_list) & Q(email__isnull=False))
            #
            # for item in email_list:
            #     print(item.email)

            email= None
            subject = request.POST['subject']
            content = request.POST['message']

            if not request.POST.get('singleEmail', None) == None:
                email = request.POST['email']


            if not request.POST.get('listFile', None) == None:
                print("Selected")
                file_loc = request.FILES['file']
                # file_loc = '/home/amir/Downloads/email_list.xlsx'
                df = pd.read_excel(file_loc)['Email']
                message = {
                    "from_email": "erp@tescan.ca",
                    "subject": subject,
                    'html': content,
                    "to": []
                }
                for item in df:
                    email_item ={
                        "email": item,
                        "type": "to"

                    }
                    message['to'].append(email_item)

                print(json.dumps(message, indent=3))
            else:
                print('Not Selected')



            # message = {
            #     "from_email": "erp@tescan.ca",
            #     "subject": subject,
            #     "text":content,
            #     "to": [
            #         {
            #             "email": email,
            #             "type": "to"
            #         }
            #     ]
            # }



            try:
                mailchimp = MailchimpTransactional.Client(MAILCHIMP_API_KEY)
                response = mailchimp.messages.send({"message": message})
                print('API called successfully: {}'.format(response))
            except ApiClientError as error:
                print('An exception occurred: {}'.format(error.text))
            # try:
            #     print("Here")
            #     mailchimp = MailchimpTransactional.Client(MAILCHIMP_API_KEY)
            #     response = mailchimp.messages.send_template(
            #         {"template_name": "test", "template_content": [{}], "message": message})
            #     print(response)
            except ApiClientError as error:
                print("An exception occurred: {}".format(error.text))


        return redirect('marketing:mailer_')



class GirdSender(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "mailer/send_mail.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']
    def get_context_data(self, *args, **kwargs):
        context = super(GirdSender, self).get_context_data()
        project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        load_dotenv(os.path.join(project_folder, '.env'))



        # message = {
        #     "from_email": "erp@tescan.ca",
        #     "subject": "Hello world",
        #     "text": "Welcome to Mailchimp Transactional!",
        #     "to": [
        #         {
        #             "email": "amirbehvandi747@gmail.com",
        #             "type": "to"
        #         }
        #     ]
        # }

        mailchimp = Mailchimp('')
        mailchimp.campaigns.send('d337a91349')
        return context



def gridSender():
    message = Mail(
        from_email='amirbehvandi747@gmail.com',
        to_emails='amirbehvandi747@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def sendMail(targetEmail,fullname=None,message=None):

    print("Start Mailing")
    msg = EmailMessage()

    asparagus_cid = make_msgid()
    msg.add_alternative("""\
       <style type="text/css">
        body {width: 600px;margin: 0 auto;}
        table {border-collapse: collapse;}
        table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;}
        img {-ms-interpolation-mode: bicubic;}
      </style>
         <style type="text/css">
        body, p, div {
          font-family: inherit;
          font-size: 14px;
        }
        body {
          color: #000000;
        }
        body a {
          color: #1188E6;
          text-decoration: none;
        }
        p { margin: 0; padding: 0; }
        table.wrapper {
          width:100% !important;
          table-layout: fixed;
          -webkit-font-smoothing: antialiased;
          -webkit-text-size-adjust: 100%;
          -moz-text-size-adjust: 100%;
          -ms-text-size-adjust: 100%;
        }
        img.max-width {
          max-width: 100% !important;
        }
        .column.of-2 {
          width: 50%;
        }
        .column.of-3 {
          width: 33.333%;
        }
        .column.of-4 {
          width: 25%;
        }
        @media screen and (max-width:480px) {
          .preheader .rightColumnContent,
          .footer .rightColumnContent {
            text-align: left !important;
          }
          .preheader .rightColumnContent div,
          .preheader .rightColumnContent span,
          .footer .rightColumnContent div,
          .footer .rightColumnContent span {
            text-align: left !important;
          }
          .preheader .rightColumnContent,
          .preheader .leftColumnContent {
            font-size: 80% !important;
            padding: 5px 0;
          }
          table.wrapper-mobile {
            width: 100% !important;
            table-layout: fixed;
          }
          img.max-width {
            height: auto !important;
            max-width: 100% !important;
          }
          a.bulletproof-button {
            display: block !important;
            width: auto !important;
            font-size: 80%;
            padding-left: 0 !important;
            padding-right: 0 !important;
          }
          .columns {
            width: 100% !important;
          }
          .column {
            display: block !important;
            width: 100% !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
          }
        }
      </style>
                     <body>
          <center class="wrapper" data-link-color="#1188E6" data-body-style="font-size:14px; font-family:inherit; color:#000000; background-color:#f0f0f0;">
            <div class="webkit">
              <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#f0f0f0">
                <tbody><tr>
                  <td valign="top" bgcolor="#f0f0f0" width="100%">
                    <table width="100%" role="content-container" class="outer" align="center" cellpadding="0" cellspacing="0" border="0">
                      <tbody><tr>
                        <td width="100%">
                          <table width="100%" cellpadding="0" cellspacing="0" border="0">
                            <tbody><tr>
                              <td>
                                <!--[if mso]>
        <center>
        <table><tr><td width="600">
      <![endif]-->
                                        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%; max-width:600px;" align="center">
                                          <tbody><tr>
                                            <td role="modules-container" style="padding:0px 0px 0px 0px; color:#000000; text-align:left;" bgcolor="#FFFFFF" width="100%" align="left"><table class="module preheader preheader-hide" role="module" data-type="preheader" border="0" cellpadding="0" cellspacing="0" width="100%" style="display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;">
        <tbody><tr>
          <td role="module-content">
            <p></p>
          </td>
        </tr>
      </tbody></table>
                                              <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:30px 0px 30px 20px;" bgcolor="#4d5171">
        <tbody>
          <tr role="module-content">
            <td height="100%" valign="top">
              <table class="column" width="560" style="width:560px; border-spacing:0; border-collapse:collapse; margin:0px 10px 0px 10px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="">
                <tbody>
                  <tr>
                    <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="a169501c-69eb-4f62-ad93-ac0150abdf03">
        <tbody>
          <tr>
            <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="left">
              <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px;" width="154" alt="" data-proportionally-constrained="true" data-responsive="false" src="http://185.231.59.78:8000/static/images/TES%20Canada%20Logo_PNG.png" >
            </td>
          </tr>
        </tbody>
      </table></td>
                  </tr>
                </tbody>
              </table>
    
            </td>
          </tr>
        </tbody>
      </table>
                                              <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="080768f5-7b16-4756-a254-88cfe5138113">
        <tbody>
          <tr>
            <td style="padding:30px 30px 0px 30px; line-height:36px; text-align:inherit; background-color:#4d5171;" height="100%" valign="top" bgcolor="#4d5171" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="color: #ffffff; font-size: 18px; font-family: inherit">Dear """ +fullname+""""</span></div><div></div></div></td>
          </tr>
        </tbody>
      </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="cddc0490-36ba-4b27-8682-87881dfbcc14">
        <tbody>
          <tr>
            <td style="padding:18px 30px 18px 30px; line-height:22px; text-align:inherit; background-color:#4d5171;" height="100%" valign="top" bgcolor="#4d5171" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="color: #ffffff; font-size: 15px">
                """ + message + """"<br>
                Kind Regards<br><br>
                TES Canada Customer Support<br>
                This is an automated email sent by the TES Canada Booking System. Please do not reply To this email. For assistance please contact TES Canada Customer Support
    
    
            </span></div><div></div></div></td>
          </tr>
        </tbody>
      </table>
                                              <table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="cd669415-360a-41a6-b4b4-ca9e149980b3">
          <tbody>
            <tr>
              <td align="center" bgcolor="#4d5171" class="outer-td" style="padding:10px 0px 40px 0px;">
                <table border="0" cellpadding="0" cellspacing="0" class="wrapper-mobile" style="text-align:center;">
                  <tbody>
                    <tr>
                    <td align="center" bgcolor="#ffc94c" class="inner-td" style="border-radius:6px; font-size:16px; text-align:center; background-color:inherit;">
    
                    </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
                                              <table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="c5a3c312-4d9d-44ff-9fce-6a8003caeeca">
        <tbody>
          <tr>
            <td style="padding:0px 20px 0px 20px;" role="module-content" height="100%" valign="top" bgcolor="#4d5171">
              <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="1px" style="line-height:1px; font-size:1px;">
                <tbody>
                  <tr>
                    <td style="padding:0px 0px 1px 0px;" bgcolor="#ffc94c"></td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
                                              <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="eb301547-da19-441f-80a1-81e1b56e64ad">
        <tbody>
          <tr>
            <td style="padding:30px 0px 18px 0px; line-height:22px; text-align:inherit; background-color:#4d5171;" height="100%" valign="top" bgcolor="#4d5171" role="module-content"><div><div style="font-family: inherit; text-align: center"><span style="color: #ffc94c; font-size: 20px; font-family: inherit"><strong></strong></span></div><div></div></div></td>
          </tr>
        </tbody>
      </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="2931446b-8b48-42bd-a70c-bffcfe784680">
        <tbody>
          <tr>
            <td style="padding:0px 0px 10px 0px;" role="module-content" bgcolor="#4d5171">
            </td>
          </tr>
        </tbody>
      </table>
    
    
    
                        </td>
                      </tr>
                    </tbody></table>
                  </td>
                </tr>
              </tbody></table>
            </div>
          </center>
    
    
    </body>
    
    
    
    
    
    
                    """, subtype='html')

    fromEmail = 'registration@tescan.ca'
    toEmail = targetEmail

    msg['Subject'] = 'Tescan Registration Dept.'
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Cc'] = 'customersupportdesk@tescan.ca'

    s = smtplib.SMTP('mail.tescan.ca', 26)
    s.starttls()
    s.login(fromEmail, 'A^f[Xoi+)ngh')
    s.send_message(msg)
    s.quit()

    print("end Mailing")
