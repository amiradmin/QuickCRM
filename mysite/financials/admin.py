from django.contrib import admin
from  financials.models import EventCandidatePayment
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class EventCandidatePaymentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','event','created_at','updated_at']
    list_filter = ['id','event','created_at','updated_at']
admin.site.register(EventCandidatePayment,EventCandidatePaymentAdmin)