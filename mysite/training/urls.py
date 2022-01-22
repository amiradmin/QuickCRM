from django.urls import path,include
from training import views





app_name ="training"
urlpatterns = [


    path('newcandidate', views.NewCandidatelView.as_view(), name='newcandidate_'),
    path('requestcourse', views.RequestView.as_view(), name='requestcourse_'),
    path('newlec', views.NewLecturerView.as_view(), name='newlec_'),
    path('canlist', views.CandidatelListView.as_view(), name='canlist_'),
    path('trainpanel', views.TrainingPanelView.as_view(), name='trainpanel_'),
    path('product', views.ProductView.as_view(), name='product_'),
    path('event', views.EventView.as_view(), name='event_'),
    path('lecturer', views.LecturerView.as_view(), name='lecturer_'),
    path('country', views.CountryView.as_view(), name='country_'),
    path('category', views.FormCategoryView.as_view(), name='category_'),
    path('updatecategory/<int:catID>', views.UpdateFormCategoryView.as_view(), name='updatecategory_'),
    path('guideline', views.FormGuidelineView.as_view(), name='guideline_'),
    path('updateguideline/<int:id>', views.UpdateFormGuidelineView.as_view(), name='updateguideline_'),
    path('delcategory/<int:pk>/delete/', views.FormCategoryDeleteView.as_view(), name='delcategory_'),
    path('delguideline/<int:pk>/delete/', views.FormGuidelineDeleteView.as_view(), name='delguideline_'),
    path('location', views.LocationView.as_view(), name='location_'),
    path('updatecan/<int:id>', views.UpdateCandidatelView.as_view(), name='updatecan_'),
    path('delcan/<int:id>', views.DeleteCandidatelView.as_view(), name='delcan_'),
    path('delevent/<int:id>', views.DeleteEventView.as_view(), name='delevent_'),
    path('updateevent/<int:id>', views.UpdateEventView.as_view(), name='updateevent_'),
    # path('event/', views.EventView.as_view(), name='event'),
    path('delpro/<int:id>', views.DeleteProductView.as_view(), name='delpro_'),
    path('updatepro/<int:id>', views.UpdateProductView.as_view(), name='updatepro_'),
    path('lecdel/<int:id>', views.DeleteLecturerView.as_view(), name='lecdel_'),
    path('updatelec/<int:id>', views.UpdateLecturerView.as_view(), name='updatelec_'),
    path('delcountry/<int:id>', views.DeleteCountryView.as_view(), name='delcountry_'),
    path('updatecountry/<int:id>', views.UpdateCountryView.as_view(), name='updatecountry_'),
    path('updateloc/<int:id>', views.UpdateLocationView.as_view(), name='updateloc_'),
    path('att/<int:id>', views.NewAttendeesView.as_view(), name='att_'),
    path('locdel/<int:id>', views.DeleteLocationView.as_view(), name='locdel_'),
    path('lecevnt/<int:id>', views.NewEventLecturerView.as_view(), name='lecevnt_'),
    path('usermonitor/<int:id>', views.UserFormMonitor.as_view(), name='usermonitor_'),
    path('addformcategory/<int:id>', views.AddFormToCategoryView.as_view(), name='addformcategory_'),


]
