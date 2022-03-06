from django.shortcuts import render, redirect
from django.views.generic import TemplateView,DeleteView
from stafftimesheet.models import Timesheet
from django.contrib.auth.models import User
from authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from training.models import TesCandidate
from datetime import datetime,date, timedelta
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
import json
# Create your views here.

class TimesheetList(LoginRequiredMixin,SidebarMixin,TemplateView):

    template_name = "timesheet/timesheet_list.html"
    group_required = u"management"
    timesheet = None
    def get_context_data(self, *args, **kwargs):

        context = super(TimesheetList, self).get_context_data()
        timesheets = Timesheet.objects.all()
        staffs = User.objects.all()
        week_start = date.today()
        week_start = week_start - timedelta(days=week_start.weekday() , weeks=1)
        print(week_start)
        week_end = week_start + timedelta(days=7)
        print(week_end)

        timesheets = Timesheet.objects.filter(
            from_temp__gte=week_start,
            from_temp__lt=week_end
        )
        staffs = User.objects.all()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        context['candidate'] =candidate
        context['staffs'] = staffs
        context['timesheets'] = timesheets
        # self.timesheet = timesheets
        # time = timesheets
        # print(self.timesheet)
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            if 'userSelection' in request.POST:
                context = super(TimesheetList, self).get_context_data()
                print("Admin List")
                userID =request.POST['userID']
                week =request.POST['week']
                # print(week)
                user = User.objects.filter(id=userID).first()

                week_start = date.today()
                week_start -= timedelta(days=week_start.weekday())
                print(week_start)
                # week_end = week_start + timedelta(days=7)
                print("Here")
                print(week.split(' to ')[0])
                week_start =week.split(' to ')[0]
                week_start_year = week_start.split('-')[2]
                week_start_month = week_start.split('-')[0]
                week_start_day = week_start.split('-')[1]
                print(week_start_year)
                print(week_start_month)
                print(week_start_day)
                week_start = week_start_year + '-' + week_start_month + '-' +week_start_day

                week_end = week.split(' to ')[1]
                week_end_year = week_end.split('-')[2]
                week_end_month = week_end.split('-')[0]
                week_end_day = week_end.split('-')[1]
                print(week_end_year)
                print(week_end_month)
                print(week_end_day)
                week_end = week_end_year + '-' + week_end_month + '-' + week_end_day
                print(week_end)
                # print(week.split(' to ')[1])
                week_start = datetime.strptime(week_start, '%Y-%m-%d')
                week_end = datetime.strptime(week_end, '%Y-%m-%d')

                timesheets = Timesheet.objects.filter(staff=user).filter(
                    from_temp__gte=week_start,
                    from_temp__lt=week_end
                )

                staffs = User.objects.all()
                candidate = TesCandidate.objects.filter(user = self.request.user).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                print(group_name)

                context['timesheets'] = timesheets
                context['staffs'] = staffs
                context['candidate'] = candidate
                context['group_name'] = group_name
                # return redirect('stafftimesheet:admintimesheetlist_' ,{'timesheets': timesheets, 'staffs':staffs, 'candidate':candidate,'group_name':group_name } )
                # return context
                return render(request, 'timesheet/timesheet_list.html',
                          {'timesheets': timesheets, 'staffs':staffs, 'candidate':candidate,'group_name':group_name } )

            else:
                print("OK OK")
                timesheetList = self.get_context_data().get('timesheets')

                for item in timesheetList:
                    obj = Timesheet.objects.filter(id=item.id).first()
                    obj.approved=True
                    obj.save()

                week_start = date.today()
                week_start -= timedelta(days=week_start.weekday())
                week_end = week_start + timedelta(days=7)

                timesheets = Timesheet.objects.filter(
                    from_temp__gte=week_start,
                    from_temp__lt=week_end
                )
                staffs = User.objects.all()
                adminStatus = False
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                for g in self.request.user.groups.all():
                    if g.name == 'super_admin' or g.name == 'training_admin':
                        adminStatus = True
                return render(request, 'timesheet/timesheet_list.html',
                          {'timesheets': timesheets ,'adminStatus':adminStatus,'staffs':staffs,'group_name':group_name })

class DeleteTimesheet(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = Timesheet
    success_url = reverse_lazy('stafftimesheet:admintimesheetlist_')

class AdminTimesheetList(LoginRequiredMixin,SidebarMixin,TemplateView):

    template_name = "timesheet/admin_apps-calendar.html"
    group_required = u"management"
    def get_context_data(self, *args, **kwargs):
        context = super(AdminTimesheetList, self).get_context_data()
        timesheets = Timesheet.objects.all()
        print(timesheets)
        staffs =User.objects.all()
        context['staffs'] = staffs
        context['timesheets'] = timesheets
        return context


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'userSelection' in request.POST:
                context = super(AdminTimesheetList, self).get_context_data()
                userID =request.POST['userID']
                user = User.objects.filter(id=userID).first()
                timesheets = Timesheet.objects.filter(staff=user)
                staffs = User.objects.all()
                print(timesheets)

                return render(request, 'timesheet/admin_apps-calendar.html',
                          {'timesheets': timesheets, 'staffs':staffs } )

            else:
                print("OK OK")
                context = super(AdminTimesheetList, self).get_context_data()
                timesheets = Timesheet.objects.all()
                dateListObj = request.POST['dateList']
                jsonDate =json.loads(dateListObj)
                print(jsonDate)
                print("================")
                deleteDateListObj = request.POST['deleteDateList']
                jsonDeleteDate =json.loads(deleteDateListObj)
                print(jsonDeleteDate)
                for i in jsonDate:

                    obj = Timesheet.objects.filter(id=i['timesheetID']).first()
                    if i['approved'] == 'approve':
                        print(i['approved'])
                        obj.approved = True
                        obj.save()
                    elif i['approved'] == 'pending':
                        obj.approved = False
                        obj.save()

                adminStatus = False
                for g in self.request.user.groups.all():
                    if g.name == 'super_admin' or g.name == 'training_admin':
                        adminStatus = True

                return render(request, 'timesheet/admin_apps-calendar.html',
                          {'timesheets': timesheets,'adminStatus':adminStatus} )


class TimesheetCalendarView(LoginRequiredMixin,SidebarMixin,TemplateView):

    template_name = "timesheet/apps-calendar.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimesheetCalendarView, self).get_context_data()
        timesheets = Timesheet.objects.filter(staff=self.request.user)
        candidate = TesCandidate.objects.filter(user = self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['timesheets'] = timesheets
        context['candidate'] = candidate
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

                dateListObj = request.POST['dateList']
                jsonDate =json.loads(dateListObj)
                print(jsonDate)

                print("Here Eddy")
                for i in jsonDate:

                    obj = Timesheet()
                    obj.staff = self.request.user
                    print(i['title']['title'])
                    print(i['title']['start'])
                    print(i['title']['end'])
                    print("====================")
                    # if len(i['startDate']) >5:
                    temp_start_year = i['title']['start'].split('-')[0]
                    temp_start_month = i['title']['start'].split('-')[1]
                    temp_start_day = i['title']['start'].split('-')[2].split('T')[0]
                    temp_start_hour  = i['title']['start'].split('-')[2].split('T')[1][:8]
                    print(temp_start_year)
                    print(temp_start_month)
                    print(temp_start_day)
                    print(temp_start_hour)
                    start_combine_date = temp_start_month + '-' + temp_start_day + '-' + temp_start_year + 'T' + temp_start_hour
                    print(start_combine_date)
                    temp_time = datetime.strptime(start_combine_date ,'%m-%d-%YT%H:%M:%S')
                    print("Exist")
                    print(temp_time)
                    date_time_obj = temp_time
                    obj.from_temp = date_time_obj
                    print("====================")
                    temp_end_year = i['title']['end'].split('-')[0]
                    temp_end_month = i['title']['end'].split('-')[1]
                    temp_end_day = i['title']['end'].split('-')[2].split('T')[0]
                    temp_end_hour  = i['title']['end'].split('-')[2].split('T')[1][:8]
                    print(temp_end_year)
                    print(temp_end_month)
                    print(temp_end_day)
                    print(temp_end_hour)
                    end_combine_date = temp_end_month + '-' + temp_end_day + '-' + temp_end_year + 'T' + temp_end_hour
                    print(end_combine_date)
                    end_temp_time = datetime.strptime(end_combine_date ,'%m-%d-%YT%H:%M:%S')
                    print("Exist")
                    print(temp_time)
                    date_time_obj = temp_time
                    obj.from_temp = date_time_obj
                    # if 'endDate'  in i:
                    #     print(i['endDate'])
                    obj.to_date = end_temp_time
                    obj.description = i['title']['title']
                    obj.task = i['title']['classNames'][0]
                    print(i['title']['classNames'][0])
                    obj.save()


                print("================")
                deleteDateListObj = request.POST['deleteDateList']
                jsonDeleteDate =json.loads(deleteDateListObj)
                print(jsonDeleteDate)
                from django.db.models import Q
                for i in jsonDeleteDate:
                    temp_start_year = i['title']['start'].split('-')[0]
                    temp_start_month = i['title']['start'].split('-')[1]
                    temp_start_day = i['title']['start'].split('-')[2].split('T')[0]
                    temp_start_hour  = i['title']['start'].split('-')[2].split('T')[1][:8]

                    print(temp_start_year)
                    print(temp_start_month)
                    print(temp_start_day)
                    print(temp_start_hour)
                    start_combine_date = temp_start_month + '-' + temp_start_day + '-' + temp_start_year + 'T' + temp_start_hour
                    print(start_combine_date)
                    temp_time = datetime.strptime(start_combine_date, '%m-%d-%YT%H:%M:%S')
                    print("Exist")
                    print(temp_time)
                    obj = Timesheet.objects.filter(Q(description = i['title']['title']) & Q(staff = self.request.user) & Q(from_temp = temp_time) ).first()

                    obj.delete()

                # for item in dateListObj:
                #     print(item.title)
                # obj = Timesheet()
                # obj.staff =User.objects.filter(id=request.POST['userID']).first()
                # obj.from_date = datetime.strptime(request.POST['from_date'], '%I:%M %p')
                # obj.to_date = datetime.strptime(request.POST['to_date'], '%I:%M %p')
                # obj.description = request.POST['description']
                #
                # obj.save()

                return redirect('stafftimesheet:timesheetcal_')




class NewTimesheetForm(LoginRequiredMixin,SidebarMixin,TemplateView):
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

                return redirect('stafftimesheet:stafftimesheetlist_', id=self.request.user.id)


        return render(request, 'forms/general/bgas.html')



class TimesheetExcelView(LoginRequiredMixin,SidebarMixin,TemplateView):
    template_name = "timesheet/timesheet_excel_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TimesheetExcelView, self).get_context_data()
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

                return redirect('stafftimesheet:stafftimesheetlist_', id=self.request.user.id)


        return render(request, 'forms/general/bgas.html')



class UpdateTimesheetForm(LoginRequiredMixin,SidebarMixin,TemplateView):
    template_name = "timesheet/update_timesheet.html"


    def get_context_data(self, *args, **kwargs):
        context = super(UpdateTimesheetForm, self).get_context_data()

        timesheet = Timesheet.objects.filter(id=self.kwargs['id']).first()
        context['timesheet'] = timesheet
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':



                obj = Timesheet.objects.filter(id=self.kwargs['id']).first()
                obj.comment =request.POST['comment']
                if not request.POST.get('approve', None) == None:
                    obj.approved =True
                else:
                    obj.approved = False
                obj.save()
                #
                # obj.save()

                return redirect('stafftimesheet:admintimesheetlist_')


        return render(request, 'forms/general/bgas.html')
