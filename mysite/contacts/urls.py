from django.urls import path,include
from contacts import views

app_name ="contacts"
urlpatterns = [


    path('newcontact/<int:id>', views.NewContactView.as_view(), name='newcontact_'),
    path('adminnewcontact', views.AdminNewContactView.as_view(), name='adminnewcontact_'),
    path('messagelist/<int:id>', views.MessageListView.as_view(), name='messagelist_'),
    path('adminmessagelist', views.AdminMessageListView.as_view(), name='adminmessagelist_'),
    path('adminoutbox', views.AdminOutboxView.as_view(), name='adminoutbox_'),
    path('candidateoutbox', views.CandidateOutboxView.as_view(), name='candidateoutbox_'),
    path('adminarchived', views.AdminArchivedView.as_view(), name='adminarchived_'),
    path('messagedetails/<int:id>', views.MessageDetailView.as_view(), name='messagedetails_'),


]
