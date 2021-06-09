from django.urls import path,include
from training import views





app_name ="training"
urlpatterns = [


    path('newcandidate', views.NewCandidatelView.as_view(), name='newcandidate_'),
    path('canlist', views.CandidatelListView.as_view(), name='canlist_'),
    path('trainpanel', views.TrainingPanelView.as_view(), name='trainpanel_'),
    path('product', views.ProductView.as_view(), name='product_'),
    path('event', views.EventView.as_view(), name='event_'),
    path('lecturer', views.LecturerView.as_view(), name='lecturer_'),
    path('country', views.CountryView.as_view(), name='country_'),
    path('location', views.LocationView.as_view(), name='location_'),
    path('updatecan/<int:id>', views.UpdateCandidatelView.as_view(), name='updatecan_'),
    path('delcan/<int:id>', views.DeleteCandidatelView.as_view(), name='delcan_'),
    path('delevent/<int:id>', views.DeleteEventView.as_view(), name='delevent_'),
    path('updateevent/<int:id>', views.UpdateEventView.as_view(), name='updateevent_'),
    path('delpro/<int:id>', views.DeleteProductView.as_view(), name='delpro_'),
    path('updatepro/<int:id>', views.UpdateProductView.as_view(), name='updatepro_'),


]
