from django.urls import path,include
from home import views





app_name ="home"
urlpatterns = [


    path('', views.HomeView.as_view(), name='home_'),


]
