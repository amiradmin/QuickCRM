"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("home.urls",namespace="home_")),
    path('training/', include("training.urls",namespace="training_")),
    path('adminpanel/', include("adminpanel.urls",namespace="adminpanel")),
    path('calender/', include("tescalendar.urls",namespace="calendar_")),
    path('map/', include("map.urls",namespace="map_")),
    path('forms/', include("forms.urls",namespace="forms_")),
    path('', include("accounting.urls",namespace="accounting")),
    path('contacts/', include("contacts.urls",namespace="contacts")),
    path('mailer/', include("mailer.urls",namespace="mailer")),
    path('ticket/', include("ticket.urls",namespace="ticket")),
    path('stafftimesheet/', include("stafftimesheet.urls",namespace="stafftimesheet_")),
    path('api/', include("api.urls",namespace="api")),
    path('api-auth/', include('rest_framework.urls')),
    path('scheduler/', include('scheduler.urls')),
    path('marketing/', include('marketing.urls')),
    path('exam_certification/', include('exam_certification.urls'))
    # path('tinymce/', include('tinymce.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
