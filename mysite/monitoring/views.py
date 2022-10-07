from django.shortcuts import render, redirect
from training.models import TesCandidate
from authorization.sidebarmixin import SidebarMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User,Group
from monitoring.models import UserMonitor,LastLogin
from django.db.models import Q, Count
from training.models import Event,TesCandidate
import datetime

class UserStatistics(GroupRequiredMixin,LoginRequiredMixin,SidebarMixin, TemplateView):
    template_name = "monitoring/user_statistics.html"
    group_required = [u'management', u'admin', u'training_admin', u'training_operator']


    def get_context_data(self, *args, **kwargs):
        context = super(UserStatistics, self).get_context_data()
        # candidate = TesCandidate.objects.filter(id=self.kwargs['canID']).first()
        candidate = TesCandidate.objects.filter(id=self.request.user.id).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        total_candidate = TesCandidate.objects.all().count()
        five_minutes_ago = datetime.datetime.now() + datetime.timedelta(minutes=-5)
        online_users = UserMonitor.objects.filter(login_date__gte=five_minutes_ago).count()
        last_login = LastLogin.objects.order_by('user','-login').distinct('user')
        user_last_login = User.objects.filter(Q(groups__name='candidates') & Q(last_login__isnull=False)).order_by('-last_login')
        login_number = LastLogin.objects\
    .all()\
    .values('user')\
    .distinct()\
    .annotate(number=Count('user'))

        last_user_list=[]
        for item in login_number:
            print(item)
            user= User.objects.filter(id=item['user']).first()
            last_user_list.append(user.username)


        date=datetime.datetime.strptime('2021-01-01', "%Y-%m-%d").date()
        print(date)
        candidates_id = Event.objects.filter(start_date__gte = date).values_list('candidate', flat=True)
        emails = TesCandidate.objects.filter(id__in = [candidates_id]).values_list('email',flat=True)
        import xlsxwriter
        row = 0
        column = 0


        workbook = xlsxwriter.Workbook('hello2.xlsx')
        worksheet = workbook.add_worksheet()


        for item in emails:
            print(item)
            worksheet.write(row, column, item)
            row += 1
        workbook.close()

        context['group_name'] = group_name
        context['candidate'] = candidate
        context['online_users'] = online_users
        context['total_candidate'] = total_candidate
        context['last_login'] = last_login
        context['login_number'] = login_number
        context['last_user_list'] = last_user_list
        context['user_last_login'] = user_last_login
        return context
