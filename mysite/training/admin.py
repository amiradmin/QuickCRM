from django.contrib import admin
from training.models import  productCategory ,StaffProfile,CandidateProfile,CourseRequest,TesCandidate,Product,FormsList,Category,Country,Location,Event,Lecturer,Certificate,Skill,WorkHistory,CandidateProject
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CourseRequestCategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','request','created_at','updated_at']
    list_filter =['id','request','created_at','updated_at']

admin.site.register(CourseRequest,CourseRequestCategoryAdmin)

class productCategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','title','created_at','updated_at']
    list_filter =['id','title','created_at','updated_at']

admin.site.register(productCategory,productCategoryAdmin)



class CandidateProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','first_name','customer_id','tes_candidate_id','email','photo','document_1','document_2','sponsor_company','contact_number','contact_number','birth_date','created_at','updated_at']
    list_filter = ['id','first_name','customer_id','tes_candidate_id','email','contact_number','birth_date','created_at','updated_at']

admin.site.register(CandidateProfile,CandidateProfileAdmin)

class TesCandidateAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','first_name','customer_id','tes_candidate_id','email','photo','document_1','document_2','contact_number','contact_number','birth_date','created_at','updated_at']
    list_filter = ['id','first_name','customer_id','tes_candidate_id','email','contact_number','birth_date','created_at','updated_at']

admin.site.register(TesCandidate,TesCandidateAdmin)


class StaffProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','first_name','email','photo','document_1','document_2','contact_number','contact_number','birth_date','created_at','updated_at']
    list_filter = ['id','first_name','email','photo','document_1','document_2','contact_number','contact_number','birth_date','created_at','updated_at']

admin.site.register(StaffProfile,StaffProfileAdmin)


# class CandidateAdmin(ImportExportModelAdmin,admin.ModelAdmin):


#     list_display = ['id','first_name','customer_id','tes_candidate_id','email','photo','document_1','document_2','sponsor_company','contact_number','contact_number','birth_date','created_at','updated_at']
#     list_filter = ['id','first_name','customer_id','tes_candidate_id','email','contact_number','birth_date','created_at','updated_at']

# admin.site.register(Candidate,CandidateAdmin)


class LecturerAdmin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ['id','first_name','last_name','passport_id','email','contact_number','city','country','photo','document_1','document_2','contact_number','city','country','contact_number','birth_date','created_at','updated_at']
    list_filter = ['id','first_name','passport_id','email','city','country','contact_number','birth_date','created_at','updated_at']

admin.site.register(Lecturer,LecturerAdmin)


class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','category','code','pic','price','type','created_at','updated_at']
    list_filter =['id','name','code','price','type','created_at','updated_at']
admin.site.register(Product,ProductAdmin)
    
class SkillAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','created_at','updated_at']
    list_filter =['id','name','created_at','updated_at']

admin.site.register(Skill,SkillAdmin)


class WorkHistoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','date','created_at','updated_at']
    list_filter =['id','name','created_at','updated_at']

admin.site.register(WorkHistory,WorkHistoryAdmin)

class CertificateAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','institute','expiryDate','issueDate','created_at','updated_at']
    list_filter =['id','name','institute','expiryDate','issueDate','created_at','updated_at']

admin.site.register(Certificate,CertificateAdmin)


class CountryAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','created_at','updated_at']
    list_filter = ['id','name','created_at','updated_at']

admin.site.register(Country,CountryAdmin)

class CandidateProjectadmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','created_at','updated_at']
    list_filter = ['id','name','created_at','updated_at']

admin.site.register(CandidateProject,CandidateProjectadmin)

class LocationAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','log','lat','country','created_at','updated_at']
    list_filter = ['id','name','country','created_at','updated_at']

admin.site.register(Location,LocationAdmin)


class EventAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    list_display = ['id','name','product','country','location','visible','start_date','announcement_type','created_at','updated_at']
    list_filter = ['id','name','product','country','location','visible','start_date','announcement_type','created_at','updated_at']

admin.site.register(Event,EventAdmin)


class FormsListAdmin(admin.ModelAdmin):
    
    list_display = ['id','name','created_at','updated_at']
    list_filter =['id','name','created_at','updated_at']

admin.site.register(FormsList,FormsListAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id','name','colorCode','created_at','updated_at']
    list_filter =['id','name','created_at','updated_at']

admin.site.register(Category,CategoryAdmin)