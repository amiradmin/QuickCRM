from django.urls import path,include
from ticket import views

app_name ="ticket"
urlpatterns = [


    path('newticket/<int:id>', views.NewTicketView.as_view(), name='newticket_'),
    path('allticket', views.TicketListView.as_view(), name='allticket_'),
    path('tickethistory/<int:id>', views.HistoryTicketView.as_view(), name='tickethistory_'),
    path('answerticket/<int:id>', views.AnswerTicketView.as_view(), name='answerticket_'),
    path('canallticket/<int:id>', views.CandidateAllTicketView.as_view(), name='canallticket_'),



]
