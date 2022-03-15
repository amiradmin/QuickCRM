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
from django.urls import reverse
from django.db.models import Q ,F ,Sum,Count
import json
# Create your views here.

class TimesheetList(LoginRequiredMixin,SidebarMixin,TemplateView):

    template_name = "timesheet/timesheet_list.html"
    group_required = u"management"
    timesheet = None
    def get_context_data(self, *args, **kwargs):

        context = super(TimesheetList, self).get_context_data()
        print("Here Here")
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
        ).annotate(durationTime=F('to_date') - F('from_temp'))

        totalHours = Timesheet.objects.annotate(durationTime=F('to_date') - F('from_temp')).aggregate(Sum('durationTime')).get('durationTime__sum')
        hours = totalHours.days * 24 + totalHours.seconds // 3600
        minutes = (totalHours.seconds % 3600) // 60
        print("total: "+str(totalHours))
        staffs = User.objects.filter(groups__name__in=['Staff','admin','training_admin','management','training_operator'])
        # staffs = User.objects.all()
        print(staffs)
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        candidate_list = TesCandidate.objects.filter(user__in=staffs).order_by('id')
        context['candidate'] =candidate
        context['idd'] =2002
        context['staffs'] = staffs
        context['timesheets'] = timesheets
        context['candidate_list'] = candidate_list
        context['totalHours'] = str(hours) +':'+str(minutes)
        # self.timesheet = timesheets
        # time = timesheets
        # print(self.timesheet)
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':



            conTotalHoursDaily = None
            if 'userSelection' in request.POST:
                context = super(TimesheetList, self).get_context_data()
                print("Admin List 0000000000")
                userID =request.POST['userID']
                user = User.objects.filter(id=userID).first()
                daily =request.POST['daily']
                task = request.POST['task']
                hours = 0
                minutes = 0

                monthSelect = request.POST['monthSelect']
                print(monthSelect)
                totalHoursDaily = 0
                totalHoursMonth = 0
                if daily is not None and monthSelect == '':
                    print("Daily")
                    q_object = ~Q()
                    if userID == "000":
                        print("All users")
                    else:
                        q_object =  Q(staff=user)
                        print("One users")



                    if(task == 'All'):
                        q_object = q_object & Q(from_temp__year=daily.split('/')[2]) & Q(
                            from_temp__month=daily.split('/')[0]) & Q(from_temp__day=daily.split('/')[1])
                    else:
                        q_object = q_object & Q(task=task) & Q(from_temp__year=daily.split('/')[2]) & Q(
                            from_temp__month=daily.split('/')[0]) & Q(from_temp__day=daily.split('/')[1])


                    timesheets = Timesheet.objects.filter(q_object
                    ).annotate(durationTime=F('to_date') - F('from_temp'))

                    totalHoursDaily = Timesheet.objects.filter(q_object).annotate(
                    durationTime=F('to_date') - F('from_temp')).aggregate(
                    Sum('durationTime')).get('durationTime__sum')
                    timesheets_task = Timesheet.objects.filter(q_object
                    ).values('task').annotate(Count('task'), durationTime=Sum(F('to_date') - F('from_temp'))).order_by()
                    print("inside")

                    timesheets_day = Timesheet.objects.filter(q_object
                    ).values('from_temp__day','from_temp__year','from_temp__month').annotate(Count('from_temp__day'), durationTime=Sum(F('to_date') - F('from_temp'))).order_by()



                    if totalHoursDaily:
                        hours = totalHoursDaily.days * 24 + totalHoursDaily.seconds // 3600
                        minutes = (totalHoursDaily.seconds % 3600) // 60
                        conTotalHoursDaily = str(hours) + ':' + str(minutes)
                else:

                    print("Monthly")
                    q_object = ~Q()
                    # print(userID)
                    if userID == "000":
                        print("All users")
                    else:
                        q_object =  Q(staff=user)
                        print("One users")

                    # q_object = q_object & Q (from_temp__month = monthSelect)
                    if(task == 'All'):
                        q_object = q_object& Q (from_temp__month = monthSelect)
                    else:
                        q_object = q_object & Q(task=task)  & Q (from_temp__month = monthSelect)

                    timesheets = Timesheet.objects.filter(q_object
                    ).annotate(durationTime=F('to_date') - F('from_temp'))

                    totalHoursMonth = Timesheet.objects.filter(q_object).annotate(durationTime=F('to_date') - F('from_temp')).aggregate(
                        Sum('durationTime')).get('durationTime__sum')
                    timesheets_task = Timesheet.objects.filter(q_object
                    ).values('task').annotate(Count('task'), durationTime=Sum(F('to_date') - F('from_temp'))).order_by()

                    timesheets_task = Timesheet.objects.filter(q_object
                    ).values('task').annotate(Count('task'), durationTime=Sum(F('to_date') - F('from_temp'))).order_by()

                    timesheets_day = Timesheet.objects.filter(q_object
                    ).values('from_temp__day','from_temp__year','from_temp__month').annotate(Count('from_temp__day'), durationTime=Sum(F('to_date') - F('from_temp'))).order_by()


                    if totalHoursMonth:
                        hours = totalHoursMonth.days * 24 + totalHoursMonth.seconds // 3600
                        minutes = (totalHoursMonth.seconds % 3600) // 60
                        conTotalHoursDaily = str(hours) + ':' + str(minutes)
                        print(totalHoursDaily)




                for item in timesheets_task:
                    print(item)



                # staffs = User.objects.all()
                candidate = TesCandidate.objects.filter(user = request.user).first()
                group_name = self.request.user.groups.values_list('name', flat=True).first()
                print(group_name)
                staffs = User.objects.filter(
                    groups__name__in=['Staff', 'admin', 'training_admin', 'management', 'training_operator'])
                candidate_list = TesCandidate.objects.filter(user__in=staffs).order_by('id')

                # context['timesheets'] = timesheets
                # context['staffs'] = staffs
                # context['candidate'] = candidate
                # context['group_name'] = group_name
                # totalHours = str(hours) + ':' + str(minutes)
                # context = {'timesheets': timesheets,'timesheets_task':timesheets_task ,'timesheets_day':timesheets_day,'staffs':staffs,'conTotalHoursDaily':conTotalHoursDaily,'task':task,'conTotalHoursDaily':conTotalHoursDaily,'candidate':candidate,'group_name':group_name ,'candidate_list':candidate_list}

                # return render(request, self.template_name, context)
                candidate = TesCandidate.objects.filter(user=self.request.user).first()
                candidate_list = TesCandidate.objects.filter(user__in=staffs).order_by('id')
                context['candidate'] = candidate
                context['timesheets_task'] = timesheets_task
                context['timesheets_day'] = timesheets_day
                context['candidate_list'] = candidate_list
                context['conTotalHoursDaily'] = conTotalHoursDaily
                context['task'] = task
                context['candidate_list'] = candidate_list
                context['conTotalHoursDaily'] = conTotalHoursDaily
                context['staffs'] = staffs
                context['timesheets'] = timesheets
                context['totalHours'] = str(hours) + ':' + str(minutes)
                context['idd'] = 6006                # self.timesheet = timesheets
                # time = timesheets
                # print(self.timesheet)
                print("Zanjan Today")
                return render(request, self.template_name, context=context)
                # return context
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
        print("Here Zanjan")
        context['group_name'] = group_name
        context['timesheets'] = timesheets
        context['candidate'] = candidate
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

                print("Radin")
                dateListObj = request.POST['dateList']
                jsonDate =json.loads(dateListObj)
                print(jsonDate)

                print("Here Eddy")
                for i in jsonDate:
                    print(i['title']['title'])
                    print(i['title']['start'])
                    print(i['title']['end'])
                    print("====================")
                    taskID = i['title']['title'].split('-')[0]
                    print(taskID)
                    # if len(i['startDate']) >5:
                    temp_start_year = i['title']['start'].split('-')[0]
                    temp_start_month = i['title']['start'].split('-')[1]
                    temp_start_day = i['title']['start'].split('-')[2].split('T')[0]
                    temp_start_hour = i['title']['start'].split('-')[2].split('T')[1][:8]
                    print(temp_start_year)
                    print(temp_start_month)
                    print(temp_start_day)
                    print(temp_start_hour)
                    start_combine_date = temp_start_month + '-' + temp_start_day + '-' + temp_start_year + 'T' + temp_start_hour
                    print(start_combine_date)
                    temp_time = datetime.strptime(start_combine_date, '%m-%d-%YT%H:%M:%S')
                    if taskID.isnumeric():
                        print("Update Task")
                        print("taskID : "+str(taskID))
                        updateEvent = Timesheet.objects.filter(id=taskID ).count()
                        if updateEvent > 0:
                            print("Update")
                            obj = Timesheet.objects.filter(id=taskID ).first()
                            obj.staff = self.request.user

                            print("Exist")
                            print(temp_time)
                            date_time_obj = temp_time
                            obj.from_temp = date_time_obj
                            print("====================")
                            temp_end_year = i['title']['end'].split('-')[0]
                            temp_end_month = i['title']['end'].split('-')[1]
                            temp_end_day = i['title']['end'].split('-')[2].split('T')[0]
                            temp_end_hour = i['title']['end'].split('-')[2].split('T')[1][:8]
                            print(temp_end_year)
                            print(temp_end_month)
                            print(temp_end_day)
                            print(temp_end_hour)
                            end_combine_date = temp_end_month + '-' + temp_end_day + '-' + temp_end_year + 'T' + temp_end_hour
                            print(end_combine_date)
                            end_temp_time = datetime.strptime(end_combine_date, '%m-%d-%YT%H:%M:%S')
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
                    else:
                        print("taskID : "+str(taskID))
                        print("New Task Event")
                        obj = Timesheet()
                        obj.staff = self.request.user

                        print("New Event")
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
                        obj.description = i['title']['title'].replace("\n", " ")
                        obj.task = i['title']['classNames'][0]
                        print(i['title']['classNames'][0])
                        obj.save()


                print("================")
                deleteDateListObj = request.POST['deleteDateList']
                jsonDeleteDate =json.loads(deleteDateListObj)
                print(jsonDeleteDate)

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
                    print("Delete")
                    print(temp_time)
                    taskID = i['title']['title'].split('-')[0]
                    print()
                    obj = Timesheet.objects.filter(id=taskID).first()

                    obj.delete()
        context = super(TimesheetCalendarView, self).get_context_data()
        timesheets = Timesheet.objects.filter(staff=self.request.user)
        candidate = TesCandidate.objects.filter(user = self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()

        context['group_name'] = group_name
        context['timesheets'] = timesheets
        context['candidate'] = candidate

        return render(request, self.template_name, context=context)
                # for item in dateListObj:
                #     print(item.title)
                # obj = Timesheet()
                # obj.staff =User.objects.filter(id=request.POST['userID']).first()
                # obj.from_date = datetime.strptime(request.POST['from_date'], '%I:%M %p')
                # obj.to_date = datetime.strptime(request.POST['to_date'], '%I:%M %p')
                # obj.description = request.POST['description']
                #
                # obj.save()






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
