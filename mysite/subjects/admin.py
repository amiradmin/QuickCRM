from django.contrib import admin
from subjects.models import Subject

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):


    list_display = ['id','code','title','created_at','updated_at']
    list_filter = ['id','code','title','created_at','updated_at']

admin.site.register(Subject,SubjectAdmin)
