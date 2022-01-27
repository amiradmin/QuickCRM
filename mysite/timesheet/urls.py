from django.urls import path,include
from timesheet import views





app_name ="timesheet"
urlpatterns = [


    path('stafftimesheetlist/<int:id>', views.TimesheetList.as_view(), name='stafftimesheetlist_'),
    path('newtimesheet/', views.NewTimesheetForm.as_view(), name='newtimesheet_'),
    path('adminstafftimesheet/', views.AdminTimesheetList.as_view(), name='adminstafftimesheet_'),


]
