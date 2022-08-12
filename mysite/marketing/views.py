from django.shortcuts import render, redirect
from authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from forms.models import CandidateForms
from training.models import TesCandidate
from django.contrib.auth.models import User, Group
from braces.views import GroupRequiredMixin
from dotenv import load_dotenv
import os
import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from exam_certification.models import CertificateAttendance,PcnCertificateProduct
import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.



class NotificationView(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/Notification_list.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']

    def get_context_data(self):
        context = super(NotificationView, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        result_list = []

        att_certifications = CertificateAttendance.objects.all()
        for item in att_certifications:
            result1 = {}
            result1['id'] = item.id
            result1['cer_number'] = item.cer_number
            result1['candidate'] = item.candidate
            result1['expired_date'] = item.issue_date + relativedelta(months = 54)
            result_list.append(result1)

        # pcn_certifications = PcnCertificateProduct.objects.all()
        # for item in pcn_certifications:
        #     result1 = {}
        #     result1['id'] = item.id
        #     result1['cer_number'] = item.cer_number
        #     result1['candidate'] = item.candidate
        #     result1['issue_date'] = item.issue_date
        #     result_list.append(result1)

        context['group_name'] = group_name
        context['candidate'] = candidate
        context['result_list'] = result_list
        return context

    def post(self, request, *args, **kwargs):
        context = super(NotificationView, self).get_context_data()
        if request.method == 'POST':
            project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            load_dotenv(os.path.join(project_folder, '.env'))
            MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')

            ids = request.POST.getlist('ids[]')
            print(ids)

            print("here")
            # message = {
            #     "from_email": "erp@tescan.ca",
            #     "subject": subject,
            #     "text": message,
            #     "to": [
            #         {
            #             "email": target_email,
            #             "type": "to"
            #         }
            #     ]
            # }
            # try:
            #     mailchimp = MailchimpTransactional.Client(MAILCHIMP_API_KEY)
            #     response = mailchimp.messages.send({"message": message})
            #     print('API called successfully: {}'.format(response))
            # except ApiClientError as error:
            #     print('An exception occurred: {}'.format(error.text))
            #

            candidate = TesCandidate.objects.filter(user=self.request.user).first()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            context['group_name'] = group_name
            context['candidate'] = candidate

            return redirect('marketing:notificationlist_')

class MailerView(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/new_mail.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']

    def get_context_data(self):
        context = super(MailerView, self).get_context_data()
        user_list =User.objects.filter(groups__name='candidates')
        candidate_list = TesCandidate.objects.filter(tes_candidate_id__isnull = False)
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        context['candidate_list'] = candidate_list
        context['group_name'] = group_name
        context['candidate'] = candidate

        return context


class NewMailchipEmail(GroupRequiredMixin,SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/new_mailchip_mail.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']

    def get_context_data(self):
        context = super(NewMailchipEmail, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate
        return context


    def post(self, request, *args, **kwargs):
        context = super(NewMailchipEmail, self).get_context_data()
        if request.method == 'POST':
            project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            load_dotenv(os.path.join(project_folder, '.env'))
            target_email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')

            message = {
                "from_email": "erp@tescan.ca",
                "subject": subject,
                "text": message,
                "to": [
                    {
                        "email": target_email,
                        "type": "to"
                    }
                ]
            }
            try:
                mailchimp = MailchimpTransactional.Client(MAILCHIMP_API_KEY)
                response = mailchimp.messages.send({"message": message})
                print('API called successfully: {}'.format(response))
            except ApiClientError as error:
                print('An exception occurred: {}'.format(error.text))


            candidate = TesCandidate.objects.filter(user=self.request.user).first()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            context['group_name'] = group_name
            context['candidate'] = candidate

            return redirect('marketing:mailer_')
