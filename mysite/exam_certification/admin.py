from django.contrib import admin
from  exam_certification.models import Invigilator,Event,Exam
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class InvigilatorProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','user','passport_id','email','document_1','document_2','contact_number','city','country','contact_number','avatar','created_at','updated_at']
    list_filter = ['id','user','passport_id','email','city','country','contact_number','avatar','created_at','updated_at']

admin.site.register(Invigilator,InvigilatorProfileAdmin)



class EventAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','exam','country','location','film','date','announcement_type','created_at','updated_at']
    list_filter = ['id','name','exam','country','location','film','date','announcement_type','created_at','updated_at']

admin.site.register(Event,EventAdmin)

class ExamAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','title','code','created_at','updated_at']
    list_filter = ['id','title','code','created_at','updated_at']

admin.site.register(Exam,ExamAdmin)
