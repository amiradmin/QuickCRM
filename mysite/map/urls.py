from django.urls import path,include
from map import views





app_name ="map"
urlpatterns = [


    path('map/', views.MapView.as_view(), name='map_'),


]
