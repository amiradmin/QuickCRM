from django.contrib import admin
from contacts.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):


    list_display = ['id','candidate','type','messageType','department','created_at','updated_at']
    list_filter = ['id','candidate','type','messageType','department','created_at','updated_at']

admin.site.register(Contact,ContactAdmin)
