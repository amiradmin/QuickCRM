from django.contrib import admin
from  exam_certification.models import Invigilator,Certificate,CertificateType
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class InvigilatorProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','user','passport_id','email','document_1','document_2','contact_number','city','country','contact_number','avatar','created_at','updated_at']
    list_filter = ['id','user','passport_id','email','city','country','contact_number','avatar','created_at','updated_at']

admin.site.register(Invigilator,InvigilatorProfileAdmin)


class CertificateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','candidate','created_at','updated_at']
    list_filter = ['id','name','event','candidate','created_at','updated_at']

admin.site.register(Certificate,CertificateAdmin)


class CertificateTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','expriation','created_at','updated_at']
    list_filter = ['id','name','expriation','created_at','updated_at']

admin.site.register(CertificateType,CertificateTypeAdmin)
