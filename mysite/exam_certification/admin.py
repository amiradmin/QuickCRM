from django.contrib import admin
from  exam_certification.models import (Invigilator,CertificateAttendance,CertificateType,CSWIPCertificateAttendance,PcnCertificateAttendance,CswipCertificateProduct,PcnCertificateProduct
                                        ,ExamMaterialPiWiModel,ExamMaterialTOFDModel1,ExamMaterialPAUTL2,ExamMaterialL3
                                        ,ExamResultPautL2,ExamMaterialTofdL3,CSWIPWeldingInspector3_1Result,
                                        CSWIPWeldingInspector3_1ExamMaterial,Samples,CSWIPWeldingInspector3_1ResultIntermadiate,
                                        CSWIPWeldingInspector3_2_1ExamMaterial,CSWIPWeldingInspector3_2_1_Result,
                                        CSWIPWeldingInspector3_2_2ExamMaterial,CSWIPWeldingInspector3_2_2_Result,
                                        BGAS_CSWIP_PaintingInspectorResult,BGAS_CSWIP_PaintingInspectorMaterial,ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP
                                        ,Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP,ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN
                                        ,Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN,PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial,
                                        PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult,PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material,
                                        PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result,TimeFlightDiffractionTOFDLevel3_CSWIP_Material,
                                        TimeFlightDiffractionTOFDLevel3_CSWIP_Result,TimeFlightDiffractionTOFDLevel3_PCN_Material,
                                        TimeFlightDiffractionTOFDLevel3_PCN_Result,RadiographicInterpretationWeldsRIMaterial,
                                        RadiographicInterpretationWeldsRIResult,DigitalRadiographicInterpretationDRI_Level2_Material,
                                        DigitalRadiographicInterpretationDRI_Level2_Result,ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN
                                        )
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCNAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN,ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCNAdmin)



class DigitalRadiographicInterpretationDRI_Level2_ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(DigitalRadiographicInterpretationDRI_Level2_Result,DigitalRadiographicInterpretationDRI_Level2_ResultAdmin)


class DigitalRadiographicInterpretationDRI_Level2_MaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(DigitalRadiographicInterpretationDRI_Level2_Material,DigitalRadiographicInterpretationDRI_Level2_MaterialAdmin)

class RadiographicInterpretationWeldsRIResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(RadiographicInterpretationWeldsRIResult,RadiographicInterpretationWeldsRIResultAdmin)

class RadiographicInterpretationWeldsRIMaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(RadiographicInterpretationWeldsRIMaterial,RadiographicInterpretationWeldsRIMaterialAdmin)

class TimeFlightDiffractionTOFDLevel3_PCN_ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(TimeFlightDiffractionTOFDLevel3_PCN_Result,TimeFlightDiffractionTOFDLevel3_PCN_ResultAdmin)

class TimeFlightDiffractionTOFDLevel3_PCN_MaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(TimeFlightDiffractionTOFDLevel3_PCN_Material,TimeFlightDiffractionTOFDLevel3_PCN_MaterialAdmin)

class TimeFlightDiffractionTOFDLevel3_CSWIP_ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(TimeFlightDiffractionTOFDLevel3_CSWIP_Result,TimeFlightDiffractionTOFDLevel3_CSWIP_ResultAdmin)



class TimeFlightDiffractionTOFDLevel3_CSWIP_MaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(TimeFlightDiffractionTOFDLevel3_CSWIP_Material,TimeFlightDiffractionTOFDLevel3_CSWIP_MaterialAdmin)


class PhasedArrayUltrasonicTesting_PAUT_L3_PCN_ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result,PhasedArrayUltrasonicTesting_PAUT_L3_PCN_ResultAdmin)


class PhasedArrayUltrasonicTesting_PAUT_L3_PCN_MaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material,PhasedArrayUltrasonicTesting_PAUT_L3_PCN_MaterialAdmin)



class PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult,PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResultAdmin)



class PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial,PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterialAdmin)


class Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCNAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN,Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCNAdmin)


class ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCNAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN,ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCNAdmin)


class Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIPAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP,Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIPAdmin)


class ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIPAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP,ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIPAdmin)

class BGAS_CSWIP_PaintingInspectorResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(BGAS_CSWIP_PaintingInspectorResult,BGAS_CSWIP_PaintingInspectorResultAdmin)

class BGAS_CSWIP_PaintingInspectorMaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(BGAS_CSWIP_PaintingInspectorMaterial,BGAS_CSWIP_PaintingInspectorMaterialAdmin)

class CSWIPWeldingInspector3_2_2_ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(CSWIPWeldingInspector3_2_2_Result,CSWIPWeldingInspector3_2_2_ResultAdmin)

class CSWIPWeldingInspector3_2_2ExamMaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(CSWIPWeldingInspector3_2_2ExamMaterial,CSWIPWeldingInspector3_2_2ExamMaterialAdmin)

class CSWIPWeldingInspector3_2_1_ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(CSWIPWeldingInspector3_2_1_Result,CSWIPWeldingInspector3_2_1_ResultAdmin)

class CSWIPWeldingInspector3_2_1ExamMaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','event','created_at','updated_at']
    list_filter = ['id','name','event','created_at','updated_at']
admin.site.register(CSWIPWeldingInspector3_2_1ExamMaterial,CSWIPWeldingInspector3_2_1ExamMaterialAdmin)

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
