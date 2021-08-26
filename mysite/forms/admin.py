from django.contrib import admin
from forms.models import Forms,Field,TwiEnrolmentForm,General,PSL30LogExp,NdtTechnique,FormList,PSL30InitialForm

# Register your models here.

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
    
    list_display = ['id','twiCandidateID','eventID','firstName','lastName','confirmation','uploadedForm','created_at','updated_at']
    list_filter =['id','twiCandidateID','eventID','firstName','lastName','created_at','updated_at']

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