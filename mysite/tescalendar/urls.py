from django.urls import path,include
from tescalendar import views





app_name ="tescalender"
urlpatterns = [


    path('cal', views.CalendarView.as_view(), name='calendar_'),


]
