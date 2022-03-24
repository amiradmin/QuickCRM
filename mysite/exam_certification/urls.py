from django.urls import path,include
from exam_certification import views
from django.conf import settings



app_name ="exam_certification"
urlpatterns = [



    path('certypelist', views.CertificateTypeView.as_view(), name='certypelist_'),


]
