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
# Create your views here.



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
