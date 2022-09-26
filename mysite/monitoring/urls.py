from django.urls import path,include
from monitoring import views
from django.conf import settings



app_name ="monitoring"
urlpatterns = [



    path('userrstatistics/', views.UserStatistics.as_view(), name='userrstatistics_'),


]
