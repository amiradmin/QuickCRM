from django.urls import path,include
from api import views
from django.conf import settings



app_name ="api"
urlpatterns = [


  
    path('getproductlist/', views.GetProductList.as_view(), name='getproductlist_'),
    path('getexams/', views.GetExamList.as_view(), name='getexams_'),

]
