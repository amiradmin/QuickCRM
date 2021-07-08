from django.contrib import admin
from forms.models import Forms
# Register your models here.



class FormsAdmin(admin.ModelAdmin):

    list_display = ['id','name','created_at','updated_at']
    list_filter =['id','name','created_at','updated_at']

admin.site.register(Forms,FormsAdmin)