from django.urls import path,include
from contacts import views

app_name ="contacts"
urlpatterns = [


    path('newcontact', views.NewContactView.as_view(), name='newcontact_'),
    path('messagelist', views.MessageListView.as_view(), name='messagelist_'),
    path('adminmessagelist', views.AdminMessageListView.as_view(), name='adminmessagelist_'),
    path('adminoutbox', views.AdminOutboxView.as_view(), name='adminoutbox_'),
    path('adminarchived', views.AdminArchivedView.as_view(), name='adminarchived_'),
    path('messagedetails/<int:id>', views.MessageDetailView.as_view(), name='messagedetails_'),


]
