from django.contrib import admin
from forms.models import (Forms,Field,TwiEnrolmentForm,General,PSL30LogExp,NdtTechnique,FormList,
                          PSL30InitialForm,NDT15AExperienceVerification,NDTCovid19,PSL57B,PSL57A,VisionTest,TesFrmCandidate,
                          TesFrmExaminationAttendance,TesLecFeedbackFrom,TesAttCandidate,TrainingAttendance,
                          TwiTrainingFeedback,TwiExamFeedback,BGAsExperienceForm)

# Register your models here.
class BGAsExperienceFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'candidate', 'eventID', 'created_at', 'updated_at']
    list_filter =['id', 'candidate', 'eventID', 'created_at', 'updated_at']
admin.site.register(BGAsExperienceForm, BGAsExperienceFormAdmin)


class TwiExamFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'candidate', 'venue','startDate','invigilator', 'created_at', 'updated_at']
    list_filter =['id', 'candidate', 'venue','startDate','invigilator', 'created_at', 'updated_at']
admin.site.register(TwiExamFeedback, TwiExamFeedbackAdmin)

class TwiTrainingFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'candidate', 'venue','startDate','lecturerName', 'created_at', 'updated_at']
    list_filter =['id', 'candidate', 'venue','startDate','lecturerName', 'created_at', 'updated_at']
admin.site.register(TwiTrainingFeedback, TwiTrainingFeedbackAdmin)

class TrainingAttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'examTitleCode', 'venue','date','lecturerName', 'created_at', 'updated_at']
    list_filter =['id', 'examTitleCode', 'venue','date','lecturerName', 'created_at', 'updated_at']
admin.site.register(TrainingAttendance, TrainingAttendanceAdmin)

class TesAttCandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'testSequence', 'candidate', 'created_at', 'updated_at']
    list_filter =['id', 'testSequence', 'candidate', 'created_at', 'updated_at']
admin.site.register(TesAttCandidate, TesAttCandidateAdmin)
# Register your models here.

class TesLecFeedbackFromAdmin(admin.ModelAdmin):
    list_display = ['id', 'courseName', 'candidate','startDate','lecturerName','location', 'created_at', 'updated_at']
    list_filter =['id', 'courseName', 'candidate','startDate','lecturerName','location', 'created_at', 'updated_at']
admin.site.register(TesLecFeedbackFrom, TesLecFeedbackFromAdmin)


class TesFrmExaminationAttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'examTitleCode', 'venue','date','invigilatorName', 'created_at', 'updated_at']
    list_filter = ['id', 'examTitleCode', 'venue','date','invigilatorName', 'created_at', 'updated_at']

admin.site.register(TesFrmExaminationAttendance, TesFrmExaminationAttendanceAdmin)

class TesFrmCandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'testSequence', 'candidate','scheme','methodOfExam', 'created_at', 'updated_at']
    list_filter =  ['id', 'testSequence', 'candidate','scheme','methodOfExam', 'created_at', 'updated_at']

admin.site.register(TesFrmCandidate, TesFrmCandidateAdmin)

class VisionTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']
    list_filter = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']

admin.site.register(VisionTest, VisionTestAdmin)


class PSL57BAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']
    list_filter = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']

admin.site.register(PSL57B, PSL57BAdmin)

class PSL57AAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']
    list_filter = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']

admin.site.register(PSL57A, PSL57AAdmin)

class NDTCovid19Admin(admin.ModelAdmin):
    list_display = ['id', 'event', 'candidate','category','fillingDate', 'created_at', 'updated_at']
    list_filter = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']

admin.site.register(NDTCovid19, NDTCovid19Admin)


class NDT15AExperienceVerificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']
    list_filter = ['id', 'event', 'candidate','category', 'created_at', 'updated_at']

admin.site.register(NDT15AExperienceVerification, NDT15AExperienceVerificationAdmin)

class GeneralAdmin(admin.ModelAdmin):
    
    list_display = ['id','event','formCategory','created_at','updated_at']
    list_filter =['id','event','formCategory','created_at','updated_at']

admin.site.register(General,GeneralAdmin)

class FormListAdmin(admin.ModelAdmin):

    list_display = ['id','name','FormID','candidate','event','category','guideline','product','status','created_at','updated_at']
    list_filter =['id','name','FormID','candidate','event','category','guideline','product','status','created_at','updated_at']

admin.site.register(FormList,FormListAdmin)

class PSL30InitialFormAdmin(admin.ModelAdmin):

    list_display = ['id','event','confirmation','candidate','email','created_at','updated_at']
    list_filter =['id','event','candidate','email','created_at','updated_at']

admin.site.register(PSL30InitialForm,PSL30InitialFormAdmin)


class TwiEnrolmentFormAdmin(admin.ModelAdmin):
    
    list_display = ['id','candidate','eventID','firstName','lastName','confirmation','uploadedForm','uploadedSign','created_at','updated_at']
    list_filter =['id','candidate','eventID','firstName','lastName','created_at','updated_at']

admin.site.register(TwiEnrolmentForm,TwiEnrolmentFormAdmin)




class FormsAdmin(admin.ModelAdmin):

    list_display = ['id','name','dbName','created_at','updated_at']
    list_filter =['id','name','dbName','created_at','updated_at']

admin.site.register(Forms,FormsAdmin)

class NdtTechniqueAdmin(admin.ModelAdmin):

    list_display = ['id','candidate','techniqueCode','employerComponent','created_at','updated_at']
    list_filter =['id','candidate','techniqueCode','employerComponent','created_at','updated_at']

admin.site.register(NdtTechnique,NdtTechniqueAdmin)

class PSL30LogExpAdmin(admin.ModelAdmin):

    list_display = ['id','fullName','ndtMethod','event','created_at','updated_at']
    list_filter =['id','fullName','ndtMethod','created_at','updated_at']

admin.site.register(PSL30LogExp,PSL30LogExpAdmin)




class FieldAdmin(admin.ModelAdmin):

    list_display = ['id','name','type','label','require','created_at','updated_at']
    list_filter =['id','name','type','require','created_at','updated_at']

admin.site.register(Field,FieldAdmin)