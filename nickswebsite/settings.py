"""
Django settings for nickswebsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from settings_secret import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = os.path.join(BASE_DIR, 'templates')
#STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
#STATIC_ROOT = (os.path.normpath(os.path.join(BASE_DIR, "static"),))
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'blog/static')
MEDIA_URL = 'http://www.nickstefan.net/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!

#set this to true when doing manage.py runserver for http://127.0.0.1:8000/
#set to false for production
LOCALDEV = False

if LOCALDEV == True:
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
else:
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = [
    '.nickstefan.net'
]



# Application definition

INSTALLED_APPS = (
    'suit',
    'markdownify',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'blog',
)

MARKDOWNIFY_WHITELIST_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'em',
    'i',
    'li',
    'ol',
    'p',
    'strong',
    'ul',
    'hr',
    'h1','h2','h3','h4','h5','h6',
    'span',
    'pre',
    'code'
]

# for DJANGO suit (ie the fancy admin)
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nickswebsite.urls'

WSGI_APPLICATION = 'nickswebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

DATE_FORMAT = 'M j Y'

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

