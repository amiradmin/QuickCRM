from django.urls import path,include
from accounting import views
from django.conf import settings



app_name ="accounting"
urlpatterns = [


    path('', views.LoginView.as_view(), name='login_'),
    path('candidatelogin', views.CandidateLoginView.as_view(), name='candidatelogin_'),
    path('profile/<int:id>', views.LecturerProfileView.as_view(), name='profile_'),
    path('staffprofile/<int:id>', views.StaffProfileView.as_view(), name='staffprofile_'),
    path('canprofile/<int:id>', views.CandidateProfileView.as_view(), name='canprofile_'),
    path('deletecer/<int:id>/<int:candidate_id>', views.DeleteCertificate.as_view(), name='deletecer_'),
    path('logout/', views.LogoutView.as_view(), name='logout_'),
    path('register/', views.RegisterView.as_view(), name='register_'),
    path('literegister/', views.LitteRegisterView.as_view(), name='literegister_'),
    path('suceess/', views.RegSuccessView.as_view(), name='suceess_'),
    # path('reset/', views.UserPasswordResetView.as_view(), name='reset_'),
    # path("reset/", views.password_reset_request, name="reset_")




]
