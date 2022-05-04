"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import platform
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j&9l(b21+5-idll%-+q#dekf)%x11%#s09j$=8@4jtx#bwrk9n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['185.231.59.78','127.0.0.1','erp.tescan.ca','www.erp.tescan.ca','72.10.172.208','192.168.1.110']

SITE_ID = 1
# Application definition Test


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'students',
    'events',
    'subjects',
    'Teachers',
    'staff',
    'notifications',
    'certification',
    'accountancy',
    'enrollment',
    'pclients',
    'forms',
    'training',
    'import_export',
    'accounting',
    'exam_certification',
    'home',
    'adminpanel',
    'tescalendar',
    'map',
    'contacts',
    'ticket',
    'rest_framework',
    'tinymce_4',
    'marketing',
    'stafftimesheet',
    'timedeltatemplatefilter',
    'scheduler',
    'sendgrid',
    'corsheaders',
    # 'scheduler.apps.SchedulerConfig'



    
]

SITE_ID = 2
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]


ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

hostName = platform.node()
print(hostName)
if hostName == 'amir-ThinkPad':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'tesdb',
            'USER': 'tes_dbuser',
            'PASSWORD': "1qaz!QAZ",
            'HOST': '185.231.59.78',
            'PORT': '5432',
        },

    }
# elif hostName == 'cloud150123.mywhc.ca':
#     DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'tesdb',
#         'USER': 'tes_dbuser',
#         'PASSWORD': "1qaz!QAZ",
#         'HOST': '185.231.59.78',
#         'PORT': '5432',
#     },
# }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'tesdb',
            'USER': 'tes_dbuser',
            'PASSWORD': "1qaz!QAZ",
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },

    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#
#
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL ="/"
LOGOUT_REDIRECT_URL = '/'

#Email


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER = 'registration@tescan.ca'
# EMAIL_HOST = 'mail.tescan.ca'  # (also tried : smtp.office365.com  and outlook.office365.com)
# EMAIL_PORT = 26
# # EMAIL_PORT = 26
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL: False
# EMAIL_HOST_PASSWORD = 'A^f[Xoi+)ngh'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'amir.behvandi@tescan.ca'
EMAIL_HOST_PASSWORD = 'Daj21372'
EMAIL_PORT = 25


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

CELERY_BROKER_URL = 'amqp://localhost'