from django.urls import path,include
from training import views





app_name ="training"
urlpatterns = [


    path('canprofile', views.CandidateProfileView.as_view(), name='canprofile_'),
    path('trainpanel', views.TrainingPanelView.as_view(), name='trainpanel_'),


]
