# -*- coding: utf-8 -*-

# Django settings for pythontr project.

import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PATH = os.path.dirname(__file__)

# Email ayarları;

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yigitsadic@gmail.com'
EMAIL_HOST_PASSWORD = '' # şşt uzaklaş bakalım ;-)
EMAIL_PORT = 587


ADMINS = (
    (u'Şahin Mersin', 'electrocoder@gmail.com'), 
    (u'Yiğit Sadıç', 'yigitsadic@gmail.com'),     
)


# Üye işlemleri ile ilgili ayarlar;

LOGIN_REDIRECT_URL = '/posts/'
LOGIN_URL = '/accounts/login/'

LOGOUT_URL = '/accounts/logout/'
AUTH_PROFILE_MODULE = 'users.Profile'


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Istanbul'

LANGUAGE_CODE = 'tr-TR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = PATH + '/media/'

MEDIA_URL = '/media/' 


STATIC_ROOT = PATH + 'static/'

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/' #'http://pythontr.org/media/admin/'

STATICFILES_DIRS = (
    PATH + '/static',
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

ROOT_URLCONF = 'pythontr_org.urls'

TEMPLATE_DIRS = (
                 PATH + '/templates',
)

# fixtures

FIXTURE_DIRS = (
                PATH + '/fixtures',
)

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
    'django.contrib.localflavor',
    'django.contrib.markup',
    
    'pythontr_org.polls',
    
    'pythontr_org.posts',
    'pythontr_org.users',
    
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
