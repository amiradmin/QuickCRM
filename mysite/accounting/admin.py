from django.contrib import admin
from accounting.models import Invoice
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class InvoiceAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','candidate','scanned_doc','receipt','balance','status','created_at','updated_at']
    list_filter = ['id','candidate','scanned_doc','receipt','balance','status','created_at','updated_at']

admin.site.register(Invoice,InvoiceAdmin)
