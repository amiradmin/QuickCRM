from django.urls import path,include
from api import views
from django.conf import settings



app_name ="api"
urlpatterns = [


  
    path('getevents/', views.GetEventList.as_view(), name='getevents_'),

]
