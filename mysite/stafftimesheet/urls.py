from django.urls import path,include
from stafftimesheet import views





app_name ="stafftimesheet"
urlpatterns = [


    path('stafftimesheetlist/<int:id>', views.TimesheetList.as_view(), name='stafftimesheetlist_'),
    path('newtimesheet/', views.NewTimesheetForm.as_view(), name='newtimesheet_'),
    path('timesheetcal/', views.TimesheetCalendarView.as_view(), name='timesheetcal_'),
    path('adminstafftimesheet/', views.AdminTimesheetList.as_view(), name='adminstafftimesheet_'),


]
