from django.contrib import admin
from students.models import Student,Degree
# Register your models here.


class StudentAdmin(admin.ModelAdmin):


    list_display = ['id','passport_id','first_name','last_name','mobile','email','degree','created_at','updated_at']
    list_filter = ['id','passport_id','first_name','last_name','mobile','email','degree','created_at','updated_at']

admin.site.register(Student,StudentAdmin)



class DegreeAdmin(admin.ModelAdmin):


    list_display = ['id','title','created_at','updated_at']
    list_filter =  ['id','title','created_at','updated_at']

admin.site.register(Degree,DegreeAdmin)
