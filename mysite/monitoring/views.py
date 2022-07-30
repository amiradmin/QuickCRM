from django.shortcuts import render, redirect
from training.models import TesCandidate
from authorization.sidebarmixin import SidebarMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User,Group
from monitoring.models import UserMonitor
import datetime

class UserStatistics(GroupRequiredMixin,LoginRequiredMixin,SidebarMixin, TemplateView):
    template_name = "monitoring/user_statistics.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']


    def get_context_data(self, *args, **kwargs):
        context = super(UserStatistics, self).get_context_data()
        # candidate = TesCandidate.objects.filter(id=self.kwargs['canID']).first()
        last_login = UserMonitor.objects.distinct('user')
        print(last_login)
        candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        five_minutes_ago = datetime.datetime.now() + datetime.timedelta(minutes=-5)
        online_users = UserMonitor.objects.filter(login_date__gte=five_minutes_ago).count()
        print(online_users)

        context['group_name'] = group_name
        context['candidate'] = candidate
        context['last_login'] = last_login
        context['online_users'] = online_users
        return context
