from django.urls import path,include
from mailer import views

app_name ="mailer"
urlpatterns = [


    path('sendmail', views.GirdSender.as_view(), name='sendmail'),
    path('singlemail', views.SingleMailSender.as_view(), name='singlemail_'),
    # path('adminnewcontact', views.AdminNewContactView.as_view(), name='adminnewcontact_'),
    # path('messagelist/<int:id>', views.MessageListView.as_view(), name='messagelist_'),
    # path('adminmessagelist', views.AdminMessageListView.as_view(), name='adminmessagelist_'),
    # path('adminoutbox', views.AdminOutboxView.as_view(), name='adminoutbox_'),
    # path('adminarchived', views.AdminArchivedView.as_view(), name='adminarchived_'),
    # path('messagedetails/<int:id>', views.MessageDetailView.as_view(), name='messagedetails_'),


]
