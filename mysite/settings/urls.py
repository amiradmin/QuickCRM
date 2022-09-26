from django.urls import path,include
from settings import views
from django.conf import settings



app_name ="settings"
urlpatterns = [



    path('sidebar/', views.SidebarView.as_view(), name='sidebar_'),


]
