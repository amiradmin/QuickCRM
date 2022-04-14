from django.contrib import admin
from  exam_certification.models import (Invigilator,CertificateAttendance,CertificateType,CSWIPCertificateAttendance,PcnCertificateAttendance,CswipCertificateProduct,PcnCertificateProduct
                                        ,ExamMaterialPiWiModel,ExamMaterialTOFDModel1,ExamMaterialPAUTL2,ExamMaterialL3
                                        ,ExamResultPautL2,ExamMaterialTofdL3,CSWIPWeldingInspector3_1Result,
                                        CSWIPWeldingInspector3_1ExamMaterial,Samples,CSWIPWeldingInspector3_1ResultIntermadiate )
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class CSWIPWeldingInspector3_1ResultIntermadiateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','primary','secondry','created_at','updated_at']
    list_filter = ['id','name','primary','secondry','created_at','updated_at']
admin.site.register(CSWIPWeldingInspector3_1ResultIntermadiate,CSWIPWeldingInspector3_1ResultIntermadiateAdmin)


class SamplesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','serial_no','asset_code','created_at','updated_at']
    list_filter = ['id','serial_no','asset_code','created_at','updated_at']
admin.site.register(Samples,SamplesAdmin)


class CSWIPWeldingInspector3_1ExamMaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(CSWIPWeldingInspector3_1ExamMaterial,CSWIPWeldingInspector3_1ExamMaterialAdmin)

class CSWIPWeldingInspector3_1ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(CSWIPWeldingInspector3_1Result,CSWIPWeldingInspector3_1ResultAdmin)

class ExamResultPautL2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamResultPautL2,ExamResultPautL2Admin)


class ExamMaterialTofdL3Admin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialTofdL3,ExamMaterialTofdL3Admin)

class ExamMaterialL3Admin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialL3,ExamMaterialL3Admin)

class ExamMaterialPAUTL2Admin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialPAUTL2,ExamMaterialPAUTL2Admin)

class ExamMaterialTOFDModelAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialTOFDModel1,ExamMaterialTOFDModelAdmin)


class ExamMaterialPiWiAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialPiWiModel,ExamMaterialPiWiAdmin)


class CSWIPCertificateAttendanceAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','candidate','created_at','updated_at']
    list_filter = ['id','name','candidate','created_at','updated_at']
admin.site.register(CSWIPCertificateAttendance,CSWIPCertificateAttendanceAdmin)


class CswipCertificateProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','created_at','updated_at']
    list_filter =   ['id','name','created_at','updated_at']
admin.site.register(CswipCertificateProduct,CswipCertificateProductAdmin)

class PcnCertificateProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','created_at','updated_at']
    list_filter =   ['id','name','created_at','updated_at']
admin.site.register(PcnCertificateProduct,PcnCertificateProductAdmin)


class InvigilatorProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','user','passport_id','email','document_1','document_2','contact_number','city','country','contact_number','avatar','created_at','updated_at']
    list_filter = ['id','user','passport_id','email','city','country','contact_number','avatar','created_at','updated_at']

admin.site.register(Invigilator,InvigilatorProfileAdmin)


class CertificateAttendanceAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','cer_number','event','candidate','created_at','updated_at']
    list_filter = ['id','name','event','candidate','created_at','updated_at']

admin.site.register(CertificateAttendance,CertificateAttendanceAdmin)

class PcnCertificateAttendanceAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','candidate','created_at','updated_at']
    list_filter = ['id','name','candidate','created_at','updated_at']
admin.site.register(PcnCertificateAttendance,PcnCertificateAttendanceAdmin)


class CertificateTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','expriation','created_at','updated_at']
    list_filter = ['id','name','expriation','created_at','updated_at']

admin.site.register(CertificateType,CertificateTypeAdmin)
