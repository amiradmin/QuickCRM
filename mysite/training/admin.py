from django.contrib import admin
from training.models import CandidateProfile
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CandidateProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','user','customer_id','passport_id','email','document_1','document_2','sponsor_company','contact_number','city','country','contact_number','birth_date','avatar','created_at','updated_at']
    list_filter = ['id','user','customer_id','passport_id','email','city','country','contact_number','birth_date','avatar','created_at','updated_at']

admin.site.register(CandidateProfile,CandidateProfileAdmin)
