from django.urls import path,include
from marketing import views

app_name ="marketing"
urlpatterns = [


    path('mailer/', views.MailerView.as_view(), name='mailer_'),
    path('newmail/', views.NewMailchipEmail.as_view(), name='newmail_'),
    path('notificationlist/', views.NotificationView.as_view(), name='notificationlist_'),



]
