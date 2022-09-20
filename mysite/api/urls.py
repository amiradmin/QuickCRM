from django.urls import path,include
from api import views
from django.conf import settings



app_name ="api"
urlpatterns = [


  
    path('getproductlist/', views.GetProductList.as_view(), name='getproductlist_'),
    path('GetEventListByproductID/<int:id>', views.GetEventListByproductID.as_view(), name='geteventlist_'),
    path('geteventbyid/<int:id>', views.GetEventByID.as_view(), name='geteventbyid_'),
    path('getproductbyID/<int:id>', views.GetProductByID.as_view(), name='getproductbyID_'),
    path('getproductbyname/', views.GetProductByName.as_view(), name='getproductbyname_'),
    path('getproductbycatid/<int:id>', views.GetCategoryProductList.as_view(), name='getproductbycatid_'),
    path('getproductbycatname/', views.GetCategoryProductListByName.as_view(), name='getproductbycatname_'),
    path('getexams/', views.GetExamList.as_view(), name='getexams_'),
    path('contact', views.NewContact.as_view(), name='contact_'),
    path('taskcontrol', views.TaskControl.as_view(), name='taskcontrol_'),

]
