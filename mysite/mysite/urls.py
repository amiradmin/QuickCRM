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
# from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #import this


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
    path('financials/', include("financials.urls",namespace="financials")),
    path('stafftimesheet/', include("stafftimesheet.urls",namespace="stafftimesheet_")),
    path('monitoring/', include("monitoring.urls",namespace="monitoring_")),
    path('api/', include("api.urls",namespace="api")),
    path('api-auth/', include('rest_framework.urls')),
    path('scheduler/', include('scheduler.urls')),
    path('marketing/', include('marketing.urls')),
    path('exam_certification/', include('exam_certification.urls')),
    # path('admin_tools_stats/', include('admin_tools_stats.urls')),

    path('accounts/', include('django.contrib.auth.urls')),


    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]

from mysite.settings import development,common
print(development.DEBUG)
if development.DEBUG:
    urlpatterns += static(common.STATIC_URL, document_root=common.STATIC_ROOT)
    urlpatterns += static(common.MEDIA_URL, document_root=common.MEDIA_ROOT)
