from django.urls import path,include
from ticket import views

app_name ="ticket"
urlpatterns = [


    path('newticket/<int:id>', views.NewTicketView.as_view(), name='newticket_'),
    path('allticket', views.TicketListView.as_view(), name='allticket_'),



]
