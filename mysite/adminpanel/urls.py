from django.urls import path,include
from adminpanel import views





app_name ="adminpanel"
urlpatterns = [


    path('adpanel', views.AdminPanelView.as_view(), name='adpanel_'),


]
