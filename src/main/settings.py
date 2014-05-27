"""
Django settings for cm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))

import wsgi

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
    'rest_framework',
    'rest_framework.authtoken',
    'api',
    'misc',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



TEMPLATE_CONTEXT_PROCESSORS = (
"django.core.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages"
    )

#ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
#ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'
#ADMIN_TOOLS_THEMING_CSS = 'css/admin_theming.css'

TRACK_AJAX_REQUESTS=True
TRACK_PAGEVIEWS=True


DEBUG_TOOLBAR_PATCH_SETTINGS = False


ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'


DATE_INPUT_FORMATS=(
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y', # '25-10-2006', '25/10/2006', '25/10/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)
DATETIME_INPUT_FORMATS=(
    '%d-%m-%Y %H:%M:%S',     # '2006-10-25 14:30:59'
    '%d-%m-%Y %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%d-%m-%Y %H:%M',        # '2006-10-25 14:30'
    '%d-%m-%Y',              # '2006-10-25'
    '%d/%m/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%d/%m/%Y %H:%M',        # '10/25/2006 14:30'
    '%d/%m/%Y',              # '10/25/2006'
    '%d/%m/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%d/%m/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%d/%m/%y %H:%M',        # '10/25/06 14:30'
    '%d/%m/%y',              # '10/25/06'
)




# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

#USE_I18N = True

#USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "main","static"),
    )

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CRISPY_FAIL_SILENTLY = not DEBUG



TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    )
}

try:
    from production_settings import *
except ImportError:
    #If production settings are present don't import local settings
    try:
        from local_settings import *
    except ImportError:
        print "couldnt import local_settings"
        pass
