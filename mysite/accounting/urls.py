from django.urls import path,include
from accounting import views





app_name ="accounting"
urlpatterns = [


    path('', views.LoginView.as_view(), name='login_'),


]
