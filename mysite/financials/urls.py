from django.urls import path,include
from financials import views

app_name ="financials"
urlpatterns = [


    path('allpayments/', views.EventCandidatePaymentView.as_view(), name='allpayments_'),
    path('newpayment', views.NewPayment.as_view(), name='newpayment_'),
    path('updatepayment/<int:id>', views.UpdatePayment.as_view(), name='updatepayment_'),
    # path('adminmessagelist', views.AdminMessageListView.as_view(), name='adminmessagelist_'),
    # path('adminoutbox', views.AdminOutboxView.as_view(), name='adminoutbox_'),
    # path('candidateoutbox', views.CandidateOutboxView.as_view(), name='candidateoutbox_'),
    # path('adminarchived', views.AdminArchivedView.as_view(), name='adminarchived_'),
    # path('messagedetails/<int:id>', views.MessageDetailView.as_view(), name='messagedetails_'),


]
