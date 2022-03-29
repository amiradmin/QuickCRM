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
    path('cswipdelete/<int:pk>/delete/', views.DeleteCswipCertificate.as_view(), name='cswipdelete_'),


]
