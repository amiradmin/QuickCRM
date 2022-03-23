from django.contrib import admin
from scheduler.models import TimesheetChecker
# Register your models here.
class TimesheetCheckerAdmin(admin.ModelAdmin):
    list_display = ['id','date','created_at','updated_at']
    list_filter = ['id','created_at','updated_at']
admin.site.register(TimesheetChecker,TimesheetCheckerAdmin)
