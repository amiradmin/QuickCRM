from django.shortcuts import render
from authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from forms.models import CandidateForms
from training.models import TesCandidate
from django.contrib.auth.models import User, Group
# Create your views here.



class MailerView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/new_mail.html"

    def get_context_data(self):
        context = super(MailerView, self).get_context_data()
        user_list =User.objects.filter(groups__name='candidates')
        print(user_list)
        candidate_list = TesCandidate.objects.filter(tes_candidate_id__isnull = False)
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        context['candidate_list'] = candidate_list
        context['group_name'] = group_name
        context['candidate'] = candidate

        return context
