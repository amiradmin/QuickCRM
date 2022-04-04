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
    # path('exampautl2delete/<int:pk>/delete/', views.DeleteExamPAUTL2.as_view(), name='exampautl2delete_'),


]
