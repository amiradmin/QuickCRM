from django.contrib import admin
from forms.models import Forms,Field,TwiEnrolmentForm

# Register your models here.


class TwiEnrolmentFormAdmin(admin.ModelAdmin):
    
    list_display = ['id','twiCandidateID','firstName','lastName','created_at','updated_at']
    list_filter =['id','twiCandidateID','firstName','lastName','created_at','updated_at']

admin.site.register(TwiEnrolmentForm,TwiEnrolmentFormAdmin)




class FormsAdmin(admin.ModelAdmin):

    list_display = ['id','name','dbName','created_at','updated_at']
    list_filter =['id','name','dbName','created_at','updated_at']

admin.site.register(Forms,FormsAdmin)




class FieldAdmin(admin.ModelAdmin):

    list_display = ['id','name','type','label','require','created_at','updated_at']
    list_filter =['id','name','type','require','created_at','updated_at']

admin.site.register(Field,FieldAdmin)