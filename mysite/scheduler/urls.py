from django.urls import path,include
from scheduler import views
from django.conf import settings



app_name ="scheduler"
urlpatterns = [


  
    path('report/', views.TaskSchedulerReport.as_view(), name='report'),


]
