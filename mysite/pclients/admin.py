from django.contrib import admin
from pclients.models import PClinet
# Register your models here.
class PClinetAdmin(admin.ModelAdmin):


    list_display = ['id','passport_id','first_name','last_name','mobile','email','created_at','updated_at']
    list_filter = ['id','passport_id','first_name','last_name','mobile','email','created_at','updated_at']

admin.site.register(PClinet,PClinetAdmin)
