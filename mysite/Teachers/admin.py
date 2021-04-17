from django.contrib import admin
from Teachers.models import Teacher,TeacherCertificate
# Register your models here.


class TeachersAdmin(admin.ModelAdmin):


    list_display = ['id','passport_id','first_name','last_name','mobile','email','created_at','updated_at']
    list_filter = ['id','passport_id','first_name','last_name','mobile','email','created_at','updated_at']

admin.site.register(Teacher,TeachersAdmin)


class TeacherCertificateAdmin(admin.ModelAdmin):


    list_display = ['id','title','created_at','updated_at']
    list_filter =  ['id','title','created_at','updated_at']

admin.site.register(TeacherCertificate,TeacherCertificateAdmin)
