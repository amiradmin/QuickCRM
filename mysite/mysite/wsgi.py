"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import request
from mysite.settings.development import *
from django.core.wsgi import get_wsgi_application
urlconf = getattr(request, "urlconf",mysite.settings.development.ROOT_URLCONF)
print(urlconf)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')
# os.environ["DJANGO_SETTINGS_MODULE"] = 'mysite.settings.development'

application = get_wsgi_application()
