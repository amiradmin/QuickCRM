from django.urls import path,include
from forms import views
from django.conf import settings



app_name ="forms"
urlpatterns = [


  
    path('newform/', views.NewForm.as_view(), name='newform_'),
    path('all/', views.AllForms.as_view(), name='all_'),
    path('allformlist/', views.AllFormsList.as_view(), name='allformlist_'),
    path('allenrolmentform/', views.AllEnrolmentForm.as_view(), name='allenrolmentform_'),
    path('updatetwienroment/<int:id>', views.UpdateTwiEnrolment.as_view(), name='updatetwienroment_'),
    path('allbgasform/', views.AllBGASForm.as_view(), name='allbgasform_'),
    path('alldb/', views.AllFormsFromPostgres.as_view(), name='alldb_'),
    path('viewform/<int:id>', views.ViewForm.as_view(), name='viewform_'),
    path('drawsig/<int:id>', views.sigDrawer.as_view(), name='drawsig_'),
    path('uploadsig/<int:id>', views.uploadSignature.as_view(), name='uploadsig_'),
    path('eachformmem/<int:id>', views.EachFormMemebr.as_view(), name='eachformmem_'),
    path('uploadform/<int:id>', views.UploadForm.as_view(), name='uploadform_'),
    path('formbyid/<int:id>', views.ViewFormByID.as_view(), name='formbyid_'),
    path('formbyformid/<int:id>', views.ViewFormByFormID.as_view(), name='formbyformid_'),
    path('formbyformidsum/<int:eventID>/<int:catID>/<int:guideID>/<int:canID>', views.ViewFormByFormIDSum.as_view(), name='formbyformidsum_'),
    path('allpslform/', views.AllPSL30LogForm.as_view(), name='allpslform_'),
    path('allpslinitialform/', views.AllBGASinitialForms.as_view(), name='allpslinitialform_'),

    path('jaegertofdl2/', views.TwiEnrolment.as_view(), name='jaegertofdl2_'),
    path('twienrolreg/<int:id>', views.TwiEnrolmentReg.as_view(), name='twienrolreg_'),
    path('psl30log/', views.PSL30LogExperienceForm.as_view(), name='psl30log_'),
    path('bgasexpform/', views.BGASExperienceForm.as_view(), name='bgasexpform_'),
    path('bgasinitailform/', views.BGASinitialForm.as_view(), name='bgasinitailform_'),
    path('formmap/', views.formMap.as_view(), name='formmap_'),
    path('formmapbyid/<slug:id>', views.FormMapByCatID.as_view(), name='formmapbyid_'),
    path('evensummary/<int:id>', views.EventSummary.as_view(), name='evensummary_'),
    path('evensummarybyformid/<int:eventID>/<int:catID>/<int:guideID>', views.EventSummaryByFormId.as_view(), name='evensummarybyformid_'),
 
    path('deltwienrol/<int:pk>/delete/', views.DeleteTwiEnrolment.as_view(), name='deltwienrol_'),
    path('delndt15a/<int:pk>/delete/', views.DeleteNdt15A.as_view(), name='delndt15a_'),
    path('ndt15expver/', views.NDT15AExperienceVerificationView.as_view(), name='ndt15expver_'),
    path('allndt15expver/', views.AllNDT15AExpVerView.as_view(), name='allndt15expver_'),
    path('getndt15byid/<int:id>', views.ViewNDT15FormByID.as_view(), name='getndt15byid_'),
    path('updatendt15/<int:id>', views.UpdateNDT15AExpVerView.as_view(), name='updatendt15_'),

]
