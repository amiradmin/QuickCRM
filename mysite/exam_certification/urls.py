from django.urls import path,include
from exam_certification import views
from django.conf import settings



app_name ="exam_certification"
urlpatterns = [



    path('cerattendancelist', views.CertificateAttendanceView.as_view(), name='cerattendancelist_'),
    path('newcerattendance', views.NewCertificateAttendance.as_view(), name='newcerattendance_'),
    path('finalcertificate/<int:id>/<int:canID>/<int:eventID>', views.FinalCertificateAttendanceView.as_view(), name='finalcertificate_'),
    path('deletecerattendance/<int:pk>/delete/', views.DeleteCertificateAttendance.as_view(), name='deletecerattendance_'),
    path('cersummary', views.CertificateSummayView.as_view(), name='cersummary_'),
    path('swipcersummary', views.CSWIPCertificateSummayView.as_view(), name='swipcersummary_'),
    path('pcncersummary', views.PCNCertificateSummayView.as_view(), name='pcncersummary_'),
    path('newpcncer', views.NewPcnCertificateAttendance.as_view(), name='newpcncer_'),
    path('newcswipcer', views.NewCswipCertificateAttendance.as_view(), name='newcswipcer_'),
    path('pcndelete/<int:pk>/delete/', views.DeletePcnCertificate.as_view(), name='pcndelete_'),


    path('exampiwi/', views.ExamMaterialPiWi.as_view(), name='exampiwi_'),
    path('exampiwisummary/', views.ExamMaterialPiWiSummary.as_view(), name='exampiwisummary_'),
    path('newexampiwi/', views.NewExamMaterialPiWi.as_view(), name='newexampiwi_'),
    path('exampiwidelete/<int:pk>/delete/', views.DeleteExamPiWi.as_view(), name='exampiwidelete_'),

    # path('exampiwi/', views.ExamMaterialPiWi.as_view(), name='exampiwi_'),
    path('examtofdsummary/', views.ExamMaterialTofdSummary.as_view(), name='examtofdsummary_'),
    path('newexamtofd/', views.NewExamMaterialTofd.as_view(), name='newexamtofd_'),
    path('examtofddelete/<int:pk>/delete/', views.DeleteExamTofd.as_view(), name='examtofddelete_'),

    path('exampautl2summary/', views.ExamMaterialPAUTL2Summary.as_view(), name='exampautl2summary_'),
    path('newexamaputl2/', views.NewExamMaterialPautl2.as_view(), name='newexamaputl2_'),
    path('exampautl2delete/<int:pk>/delete/', views.DeleteExamPAUTL2.as_view(), name='exampautl2delete_'),

    path('examl3summary/', views.ExamMaterialL3Summary.as_view(), name='examl3summary_'),
    path('newexaml3/', views.NewExamMaterialL3.as_view(), name='newexaml3_'),
    path('l3ismform/<int:id>', views.ExamMaterialL3IMSForm.as_view(), name='l3ismform_'),
    path('examl3delete/<int:pk>/delete/', views.DeleteExamL3Material.as_view(), name='examl3delete_'),

    path('examtofdl3summary/', views.ExamMaterialTofdL3Summary.as_view(), name='examtofdl3summary_'),
    path('newexamtofdl3/', views.NewExamMaterialTofdL3.as_view(), name='newexamtofdl3_'),
    path('tofdl3ismform/<int:id>', views.ExamMaterialTofdL3IMSForm.as_view(), name='tofdl3ismform_'),
    path('examtofdl3delete/<int:pk>/delete/', views.DeleteExamTofdL3Material.as_view(), name='examtofdl3delete_'),

    path('examresultsummary/', views.ExamResultSummary.as_view(), name='examresultsummary_'),
    path('newexamresult/', views.NewExamResultPautL2.as_view(), name='newexamresult_'),
    path('newexamresultbyid/<int:id>', views.ExamResultSummaryByID.as_view(), name='newexamresultbyid_'),
    # path('l3ismform/<int:id>', views.ExamMaterialL3IMSForm.as_view(), name='l3ismform_'),
    # path('examl3delete/<int:pk>/delete/', views.DeleteExamL3Material.as_view(), name='examl3delete_'),

    path('examscwip31summary/', views.CSWIPExamMaterial31Summary.as_view(), name='examscwip31summary_'),
    path('newcswipexam31/', views.NewCSWIPExamMaterial31.as_view(), name='newcswipexam31_'),
    path('examcswip31delete/<int:pk>/delete/', views.DeleteCSWIPExamMaterial31.as_view(), name='examcswip31delete_'),


    path('examscwip31resultsummary/', views.CSWIPExamResult31Summary.as_view(), name='examscwip31resultsummary_'),
    path('newcswipexam31result/', views.NewExamResultSwip31.as_view(), name='newcswipexam31result_'),
    # path('examcswip31delete/<int:pk>/delete/', views.DeleteCSWIPExamMaterial31.as_view(), name='examcswip31delete_'),


]
