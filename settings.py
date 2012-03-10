# -*- coding: utf-8 -*-

# Django settings for pythontr project.

import os.path

PATH = os.path.dirname(__file__)

EMAIL_HOST = 'xxx.xxx.com'
EMAIL_PORT = xxx
 
EMAIL_HOST_USER = 'xxxxxx@xxxx.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxx'
 
EMAIL_USE_TLS = True

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('xxx', 'xxx@xxxx.xxx'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Istanbul'

LANGUAGE_CODE = 'tr-TR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = PATH + '/static_media/'


MEDIA_URL = '/media/'


STATIC_ROOT = PATH + '/static/'

STATIC_URL = 'http://pythontr.org/static/'

ADMIN_MEDIA_PREFIX = 'http://pythontr.org/media/admin/'

STATICFILES_DIRS = (
    DIRNAME + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '8!xvqfrfretert45564y6565655566ythhhhhh&k0c@ru)v'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

TEMPLATE_DIRS = ("/home/electrocoder/webapps/pythontr_org/myproject/templates")

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

DISQUS_API_KEY = 'rr3r45gg7hoAnpar32erwr32432rerSLlxoos2JpnY' 
DISQUS_WEBSITE_SHORTNAME = 'pythonprogramcilari'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.admin',

    'pythontr_org.polls',
    'pythontr_org.python',
    'pythontr_org.pythoncoders',
    'pythontr_org.pythonauthors',
    
    'disqus',    
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
