from django.contrib import admin
from staff.models import Staff,Section
# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','section','mobile','email','created_at']
    list_filter = ['id','user','first_name','last_name','section','mobile','email','created_at']
admin.site.register(Staff,StaffAdmin )




class SectionAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']
    list_filter = ['id','title','created_at']
admin.site.register(Section,SectionAdmin )
