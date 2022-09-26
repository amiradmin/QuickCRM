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
BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j&9l(b21+5-idll%-+q#dekf)%x11%#s09j$=8@4jtx#bwrk9n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','erp.tescan.ca','www.erp.tescan.ca','72.10.172.208','https://erp.tescan.ca']

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
    'django_login_history',
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
    'financials',
    'pytest',
    'crispy_forms',
    'activity_log',
    'monitoring',
    'settings'








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
     # 'monitoring.middleware.OnlineNowMiddleware',
    "mysite.custom_middleware.LastActivityMiddleware",  # add custom middleware
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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

AUTHENTICATION_BACKENDS = ('accounting.backends.CaseInsensitiveModelBackend', )
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

hostName = platform.node()
# print(hostName)
if hostName == 'amir-ThinkPad':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'testdb_development',
            'USER': 'tes_dbuser',
            'PASSWORD': "1qaz!QAZ",
            'HOST': '127.0.0.1',
            'PORT': '5432',
            'TEST': {
                'NAME': 'test_db_6',
            },
            # 'logs': {
            #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
            #     'NAME': 'testdb',
            #     'USER': 'tes_dbuser',
            #     'PASSWORD': "1qaz!QAZ",
            #     'HOST': '127.0.0.1',
            #     'PORT': '5432',
            # },
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
            'NAME': 'testdb',
            'USER': 'tes_dbuser',
            'PASSWORD': "Eddy747today2022",
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },
        # 'logs': {
        #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #     'NAME': 'testdb',
        #     'USER': 'tes_dbuser',
        #     'PASSWORD': "1qaz!QAZ",
        #     'HOST': '127.0.0.1',
        #     'PORT': '5432',
        # },


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

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#
#
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR.parent.parent, 'media/')
print('here')
print(MEDIA_ROOT)
print('here')



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
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'erp@tescan.ca'
EMAIL_HOST_PASSWORD = 'Wuh28931'
EMAIL_PORT = 25
# DEFAULT_FROM_EMAIL = 'erp@tescan.ca'
# #
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER ='amirbehvandi747@gmail.com'
# EMAIL_HOST_PASSWORD = 'Tempo@747??Edward&&Sahar3'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'amirbehvandi747@gmail.com'
# EMAIL_HOST_PASSWORD = 'Tempo@747??Edward&&Sahar3'



CELERY_BROKER_URL = 'amqp://localhost'


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True



# For writing log to another DB

DATABASE_ROUTERS = ['activity_log.router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'activity_log': 'logs'}


# Create DB automatically (for postgres, and may be mysql).
# We create log database automatically using raw SQL in pre_migrate signal.
# You must insure, that DB user has permissions for creation databases.
# Tested only for postgresql
ACTIVITYLOG_AUTOCREATE_DB = False

# App settings

# Log anonimus actions?
ACTIVITYLOG_ANONIMOUS = True

# Update last activity datetime in user profile. Needs updates for user model.
ACTIVITYLOG_LAST_ACTIVITY = True

# Only this methods will be logged
ACTIVITYLOG_METHODS = ('POST', 'GET')

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
ACTIVITYLOG_STATUSES = (200, )

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
# ACTIVITYLOG_EXCLUDE_STATUSES = (302, )

# URL substrings, which ignores
ACTIVITYLOG_EXCLUDE_URLS = ('/admin/activity_log/activitylog', )


handler404 = 'mysite.views.entry_not_found'
