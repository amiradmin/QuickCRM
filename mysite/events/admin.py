from django.contrib import admin
from events.models import Event
# Register your models here.
class EventAdmin(admin.ModelAdmin):


    list_display = ['id','title','duration','duration','location','start_date','created_at','updated_at']
    list_filter =  ['id','title','duration','duration','location','start_date','created_at','updated_at']

admin.site.register(Event,EventAdmin)
