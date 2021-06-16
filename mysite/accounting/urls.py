from django.urls import path,include
from accounting import views





app_name ="accounting"
urlpatterns = [


    path('', views.LoginView.as_view(), name='login_'),
    path('profile/<int:id>', views.LecturerProfileView.as_view(), name='profile_'),
    path('canprofile/<int:id>', views.CandidateProfileView.as_view(), name='canprofile_'),


]
