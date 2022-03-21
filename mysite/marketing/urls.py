from django.urls import path,include
from marketing import views

app_name ="marketing"
urlpatterns = [


    path('mailer/', views.MailerView.as_view(), name='mailer_'),



]
