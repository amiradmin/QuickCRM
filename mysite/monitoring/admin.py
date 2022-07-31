from django.contrib import admin
from  monitoring.models import UserMonitor,LastLogin
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class UserMonitorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','user','login_date','created_at','updated_at']
    list_filter = ['id','user','login_date','created_at','updated_at']
admin.site.register(UserMonitor,UserMonitorAdmin)



class LastLoginAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','user','login','created_at','updated_at']
    list_filter = ['id','user','login','created_at','updated_at']
admin.site.register(LastLogin,LastLoginAdmin)
