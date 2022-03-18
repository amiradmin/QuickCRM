from django.urls import path,include
from stafftimesheet import views





app_name ="stafftimesheet"
urlpatterns = [


    path('admintimesheetlist/', views.TimesheetList.as_view(), name='admintimesheetlist_'),
    path('newtimesheet/', views.NewTimesheetForm.as_view(), name='newtimesheet_'),
    path('timesheetcal/', views.TimesheetCalendarView.as_view(), name='timesheetcal_'),
    path('adminstafftimesheet/', views.AdminTimesheetList.as_view(), name='adminstafftimesheet_'),
    path('updatetimesheet/<int:id>', views.UpdateTimesheetForm.as_view(), name='updatetimesheet_'),
    path('deltimesheet/<int:pk>/delete/', views.DeleteTimesheet.as_view(), name='deltimesheet_'),
    path('timesheetims/', views.TimesheetExcelView.as_view(), name='timesheetims_'),
    path('timesheetimalert/', views.TimesheetAlertView.as_view(), name='timesheetimalert_'),





]
