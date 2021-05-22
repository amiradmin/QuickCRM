from django.urls import path,include
from training import views





app_name ="training"
urlpatterns = [


    path('canprofile', views.CandidatelView.as_view(), name='canprofile_'),
    path('trainpanel', views.TrainingPanelView.as_view(), name='trainpanel_'),
    path('product', views.ProductView.as_view(), name='product_'),
    path('event', views.EventView.as_view(), name='event_'),
    path('lecturer', views.LecturerView.as_view(), name='lecturer_'),
    path('country', views.CountryView.as_view(), name='country_'),
    path('location', views.LocationView.as_view(), name='location_'),


]
