from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from timesheet.models import Timesheet
from django.contrib.auth.models import User
from authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
import json
# Create your views here.

class TimesheetList(LoginRequiredMixin,SidebarMixin,TemplateView):

    template_name = "timesheet/timesheet_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimesheetList, self).get_context_data()
        user = User.objects.filter(id=self.kwargs['id']).first()
        timesheets = Timesheet.objects.filter(staff=user)
        user = User.objects.filter(id=self.request.user.id).first()
        context['user'] = user
        context['timesheets'] = timesheets
        return context


class AdminTimesheetList(LoginRequiredMixin,SidebarMixin,TemplateView):

    template_name = "timesheet/admin_timesheet_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AdminTimesheetList, self).get_context_data()
        timesheets = Timesheet.objects.all()
        context['timesheets'] = timesheets
        return context


class TimesheetCalendarView(LoginRequiredMixin,SidebarMixin,TemplateView):

    template_name = "timesheet/apps-calendar.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimesheetCalendarView, self).get_context_data()
        timesheets = Timesheet.objects.all()
        context['timesheets'] = timesheets
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

                dateListObj = request.POST['dateList']

                # for item in dateListObj:
                jsonDate =json.loads(dateListObj)
                # print(jsonDate)

                for i in jsonDate:
                    print(i)
                # for item in dateListObj:
                #     print(item.title)
                # obj = Timesheet()
                # obj.staff =User.objects.filter(id=request.POST['userID']).first()
                # obj.from_date = datetime.strptime(request.POST['from_date'], '%I:%M %p')
                # obj.to_date = datetime.strptime(request.POST['to_date'], '%I:%M %p')
                # obj.description = request.POST['description']
                #
                # obj.save()

                return redirect('timesheet:timesheetcal_')




class NewTimesheetForm(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "timesheet/new_timesheet.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewTimesheetForm, self).get_context_data()
        user = User.objects.filter(id=self.request.user.id).first()
        context['user'] = user
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':



                obj = Timesheet()
                obj.staff =User.objects.filter(id=request.POST['userID']).first()
                obj.from_date = datetime.strptime(request.POST['from_date'], '%I:%M %p')
                obj.to_date = datetime.strptime(request.POST['to_date'], '%I:%M %p')
                obj.description = request.POST['description']

                obj.save()

                return redirect('timesheet:stafftimesheetlist_', id=self.request.user.id)


        return render(request, 'forms/general/bgas.html')
