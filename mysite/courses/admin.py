from django.contrib import admin
from courses.models import Courses
# Register your models here.
class CoursesAdmin(admin.ModelAdmin):


    list_display = ['id','title','duration','duration','location','start_date','created_at','updated_at']
    list_filter =  ['id','title','duration','duration','location','start_date','created_at','updated_at']

admin.site.register(Courses,CoursesAdmin)
