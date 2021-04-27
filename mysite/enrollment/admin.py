from django.contrib import admin
from enrollment.models import Enrollment
# Register your models here.
class EnrollmentAdmin(admin.ModelAdmin):


    list_display = ['id','title','student','exam_date','created_at','updated_at']
    list_filter =  ['id','title','student','exam_date','created_at','updated_at']

# admin.site.register(Enrollment,EnrollmentAdmin)
