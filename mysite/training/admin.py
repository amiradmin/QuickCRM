from django.contrib import admin
from training.models import CandidateProfile,Product,Country,Location,Event,Lecturer
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CandidateProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','first_name','customer_id','tes_candidate_id','email','photo','document_1','document_2','sponsor_company','contact_number','city','country','contact_number','birth_date','created_at','updated_at']
    list_filter = ['id','first_name','customer_id','tes_candidate_id','email','city','country','contact_number','birth_date','created_at','updated_at']

admin.site.register(CandidateProfile,CandidateProfileAdmin)

class LecturerAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','first_name','last_name','passport_id','email','photo','document_1','document_2','contact_number','city','country','contact_number','birth_date','created_at','updated_at']
    list_filter = ['id','first_name','passport_id','email','city','country','contact_number','birth_date','created_at','updated_at']

admin.site.register(Lecturer,LecturerAdmin)


class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','code','price','type','created_at','updated_at']
    list_filter =['id','name','code','price','type','created_at','updated_at']

admin.site.register(Product,ProductAdmin)


class CountryAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','created_at','updated_at']
    list_filter = ['id','name','created_at','updated_at']

admin.site.register(Country,CountryAdmin)



class LocationAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','log','lat','country','created_at','updated_at']
    list_filter = ['id','name','country','created_at','updated_at']

admin.site.register(Location,LocationAdmin)


class EventAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','product','country','location','start_date','announcement_type','created_at','updated_at']
    list_filter = ['id','name','product','country','location','start_date','announcement_type','created_at','updated_at']

admin.site.register(Event,EventAdmin)
