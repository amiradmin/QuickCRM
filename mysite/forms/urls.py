from django.urls import path,include
from forms import views
from django.conf import settings



app_name ="forms"
urlpatterns = [


  
    path('newform/', views.NewForm.as_view(), name='newform_'),
    path('all/', views.AllForms.as_view(), name='all_'),
    path('allformlist/', views.AllFormsList.as_view(), name='allformlist_'),

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

    path('newtwienrolment/', views.TwiEnrolment.as_view(), name='jaegertofdl2_'),
    path('allenrolmentform/', views.AllEnrolmentForm.as_view(), name='allenrolmentform_'),
    path('updatetwienroment/<int:id>', views.UpdateTwiEnrolment.as_view(), name='updatetwienroment_'),

    path('twienrolreg/<int:id>', views.TwiEnrolmentReg.as_view(), name='twienrolreg_'),

    path('bgasexpform/', views.BGASExperienceForm.as_view(), name='bgasexpform_'),


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
    path('deletelecfedform/<int:pk>/delete/', views.DeleteLecFeedbackForm.as_view(), name='deletelecfedform_'),
    path('updatelecfedform/<int:id>', views.UpdateLecFeedbackForm.as_view(), name='updatelecfedform_'),
    path('viewlecfedform/<int:id>', views.ViewLecFeedbackForm.as_view(), name='viewlecfedform_'),



    path('newtrainingatt/', views.NewTrainingAttendance.as_view(), name='newtrainingatt_'),
    path('alltrainingatt/', views.AllTrainingAttendance.as_view(), name='alltrainingatt_'),
    path('deletetrainingatt/<int:pk>/delete/', views.DeleteTrainingAttendance.as_view(), name='deletetrainingatt_'),
    path('updatetrainingatt/<int:id>', views.UpdateTrainingAttendancem.as_view(), name='updatetrainingatt_'),
    path('viewtrainingatt/<int:id>', views.ViewTrainingAttendance.as_view(), name='viewtrainingatt_'),


    path('newtwitrainingfeed/', views.NewTWITrainingFeedback.as_view(), name='newtwitrainingfeed_'),
    path('alltwitrainingfeed/', views.AllTWITrainingFeedback.as_view(), name='alltwitrainingfeed_'),
    path('deletetwitrainingfeed/<int:pk>/delete/', views.DeleteTWITrainingFeedback.as_view(), name='deletetwitrainingfeed_'),
    path('updatetwitrainingfeed/<int:id>', views.UpdateTWITrainingFeedback.as_view(), name='updatetwitrainingfeed_'),
    path('viewtwitrainingfeed/<int:id>', views.ViewTWITrainingFeedback.as_view(), name='viewtwitrainingfeed_'),


    path('newtwiexamfeed/', views.NewTWIExamFeedback.as_view(), name='newtwiexamfeed_'),
    path('alltwiexamfeed/', views.AllTWIExamFeedback.as_view(), name='alltwiexamfeed_'),
    path('deletetwiexamfeed/<int:pk>/delete/', views.DeleteTWIExamFeedback.as_view(), name='deletetwiexamfeed_'),
    path('updatetwiexamfeed/<int:id>', views.UpdateTWIExamFeedback.as_view(), name='updatetwiexamfeed_'),
    path('viewtwiexamfeed/<int:id>', views.ViewTWIExamFeedback.as_view(), name='viewtwiexamfeed_'),

    path('psl30log/', views.PSL30LogExperienceForm.as_view(), name='psl30log_'),
    path('deletepsl3logexp/<int:pk>/delete/', views.DeletePSL30LogExperienceForm.as_view(), name='deletepsl3logexp_'),
    path('updatepsl3logexp/<int:id>', views.UpdatePSL30LogExperienceForm.as_view(), name='updatepsl3logexp_'),
    path('viewpsl3logexp/<int:id>', views.ViewPSL30LogExperienceForm.as_view(), name='viewpsl3logexp_'),
    path('msgupdatepsl3logexp/<int:id>/<int:msgID>', views.MessagePSL30LogExperienceForm.as_view(), name='msgupdatepsl3logexp_'),

    path('newpsl57A/', views.PSL57AFOrmView.as_view(), name='newpsl57A_'),
    path('allpsl57A/', views.AllPSL57AFOrmView.as_view(), name='allpsl57A_'),
    path('updatepsl57A/<int:id>', views.UpdatePSL57AForm.as_view(), name='updatepsl57A_'),
    path('messageupdatepsl57A/<int:id>/<int:msgID>', views.MessageUpdatePSL57AForm.as_view(), name='messageupdatepsl57A'),
    path('viewpsl57A/<int:id>', views.ViewPSL57AForm.as_view(), name='viewpsl57A_'),
    path('deletepsl57A/<int:pk>/delete/', views.DeletePSL57AForm.as_view(), name='deletepsl57A_'),


    path('ndtcovid/', views.NDTCovid19View.as_view(), name='ndtcovid_'),
    path('allndtcovid19/', views.AllNDT15Covid19View.as_view(), name='allndtcovid19_'),
    path('covidbyid/<int:id>', views.ViewNDTCovid19FormByID.as_view(), name='covidbyid_'),
    path('updatecovid19/<int:id>', views.UpdateNDTCovid19View.as_view(), name='updatecovid19_'),
    path('msgupdatecovid19/<int:id>/<int:msgID>', views.MSGUpdateNDTCovid19View.as_view(),name='msgupdatecovid19_'),
]
