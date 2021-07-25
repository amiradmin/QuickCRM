from django.urls import path,include
from forms import views
from django.conf import settings



app_name ="forms"
urlpatterns = [


  
    path('newform/', views.NewForm.as_view(), name='newform_'),
    path('all/', views.AllForms.as_view(), name='all_'),
    path('allformlist/', views.AllFormsList.as_view(), name='allformlist_'),
    path('allenrolmentform/', views.AllEnrolmentForm.as_view(), name='allenrolmentform_'),
    path('alldb/', views.AllFormsFromPostgres.as_view(), name='alldb_'),
    path('viewform/<int:id>', views.ViewForm.as_view(), name='viewform_'),
    path('drawsig/<int:id>', views.sigDrawer.as_view(), name='drawsig_'),
    path('uploadsig/<int:id>', views.uploadSignature.as_view(), name='uploadsig_'),
    path('eachformmem/<int:id>', views.EachFormMemebr.as_view(), name='eachformmem_'),
    path('uploadform/<int:id>', views.UploadForm.as_view(), name='uploadform_'),
    path('formbyid/<int:id>', views.ViewFormByID.as_view(), name='formbyid_'),
    path('formbyformid/<int:id>', views.ViewFormByFormID.as_view(), name='formbyformid_'),
    
    path('jaegertofdl2/', views.TwiEnrolment.as_view(), name='jaegertofdl2_'),
    path('formmap/', views.formMap.as_view(), name='formmap_'),
    path('formmapbyid/<slug:id>', views.FormMapByCatID.as_view(), name='formmapbyid_'),
    path('evensummary/', views.EventSummary.as_view(), name='evensummary_'),
 


]
