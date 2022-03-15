from django.contrib import admin
from stafftimesheet.models import Timesheet
# Register your models here.
class TimesheetAdmin(admin.ModelAdmin):


    list_display = ['id','staff','description','task','duration','approved','created_at','updated_at']
    list_filter = ['id','staff','description','duration','approved','created_at','updated_at']

admin.site.register(Timesheet,TimesheetAdmin)
