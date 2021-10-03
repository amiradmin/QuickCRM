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
    path('delecovid19/<int:pk>/delete/', views.DeleteCovid19.as_view(), name='delecovid19_'),
    path('delpcl57b/<int:pk>/delete/', views.DeletePSL57B.as_view(), name='delpcl57b_'),
    path('ndt15expver/', views.NDT15AExperienceVerificationView.as_view(), name='ndt15expver_'),
    path('allndt15expver/', views.AllNDT15AExpVerView.as_view(), name='allndt15expver_'),
    path('getndt15byid/<int:id>', views.ViewNDT15FormByID.as_view(), name='getndt15byid_'),
    path('updatendt15/<int:id>', views.UpdateNDT15AExpVerView.as_view(), name='updatendt15_'),
    path('ndtcovid/', views.NDTCovid19View.as_view(), name='ndtcovid_'),
    path('allndtcovid19/', views.AllNDT15Covid19View.as_view(), name='allndtcovid19_'),
    path('covidbyid/<int:id>', views.ViewNDTCovid19FormByID.as_view(), name='covidbyid_'),
    path('updatecovid19/<int:id>', views.UpdateNDTCovid19View.as_view(), name='updatecovid19_'),


    path('psl57b/', views.NewPSL57B.as_view(), name='psl57b_'),
    path('allpsl57b/', views.AllPSL57BView.as_view(), name='allpsl57b_'),
    path('updatepsl57b/<int:id>', views.UpdatePSL57B.as_view(), name='updatepsl57b_'),
    path('viewpsl57b/<int:id>', views.ViewPSL57B.as_view(), name='viewpsl57b_'),

    path('newvisiontest/', views.NewVisionTest.as_view(), name='newvisiontest_'),
    path('allisiontest/', views.AllVisionTestView.as_view(), name='allisiontest_'),
    path('visionview/<int:id>', views.ViewVitionTest.as_view(), name='visionview_'),
    path('delvision/<int:pk>/delete/', views.DeleteVisionTest.as_view(), name='delvision_'),
    path('updatevision/<int:id>', views.updateVisionTest.as_view(), name='updatevision_'),


    path('tesfrmexamattend/', views.NewTesFrmExaminationAttendance.as_view(), name='tesfrmexamattend_'),
    path('alltesfrmexamattend/', views.AllTesFrmExaminationAttendance.as_view(), name='alltesfrmexamattend_'),
    path('deletetesfrmexamattend/<int:pk>/delete/', views.DeleteTesFrmExaminationAttendance.as_view(), name='deletetesfrmexamattend_'),
    path('updatetesfrmexamattend/<int:id>', views.UpdateTesFrmExaminationAttendance.as_view(), name='updatetesfrmexamattend_'),
    path('viewtesfrmexamattend/<int:id>', views.ViewTesFrmExaminationAttendance.as_view(), name='viewtesfrmexamattend_'),


    path('newlecfedform/', views.NewLecFeedbackForm.as_view(), name='newlecfedform_'),
    path('alllecfedform/', views.AllLecFeedbackForm.as_view(), name='alllecfedform_'),

]
