from django.contrib import admin
from forms.models import Forms,Field,TwiEnrolmentForm,General,PSL30LogExp

# Register your models here.

class GeneralAdmin(admin.ModelAdmin):
    
    list_display = ['id','event','formCategory','created_at','updated_at']
    list_filter =['id','event','formCategory','created_at','updated_at']

admin.site.register(General,GeneralAdmin)

class TwiEnrolmentFormAdmin(admin.ModelAdmin):
    
    list_display = ['id','twiCandidateID','eventID','firstName','lastName','confirmation','uploadedForm','created_at','updated_at']
    list_filter =['id','twiCandidateID','eventID','firstName','lastName','created_at','updated_at']

admin.site.register(TwiEnrolmentForm,TwiEnrolmentFormAdmin)




class FormsAdmin(admin.ModelAdmin):

    list_display = ['id','name','dbName','created_at','updated_at']
    list_filter =['id','name','dbName','created_at','updated_at']

admin.site.register(Forms,FormsAdmin)

class PSL30LogExpAdmin(admin.ModelAdmin):

    list_display = ['id','fullname','ndtMethod','eventID','created_at','updated_at']
    list_filter =['id','fullname','ndtMethod','created_at','updated_at']

admin.site.register(PSL30LogExp,PSL30LogExpAdmin)




class FieldAdmin(admin.ModelAdmin):

    list_display = ['id','name','type','label','require','created_at','updated_at']
    list_filter =['id','name','type','require','created_at','updated_at']

admin.site.register(Field,FieldAdmin)