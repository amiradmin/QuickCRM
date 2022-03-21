from django.shortcuts import render
from authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from forms.models import CandidateForms
from training.models import TesCandidate
# Create your views here.



class MailerView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "marketing/new_mail.html"

    def get_context_data(self):
        context = super(MailerView, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        context['group_name'] = group_name
        context['candidate'] = candidate

        self.candidateID = 50
        return context
