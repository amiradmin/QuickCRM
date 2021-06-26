from django.urls import path,include
from forms import views
from django.conf import settings



app_name ="forms"
urlpatterns = [


  
    path('newform/', views.NewForm.as_view(), name='newform_'),
 


]
