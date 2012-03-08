# Django settings for pythontr project.

import os

DIRNAME = os.path.dirname(__file__)

<<<<<<< HEAD
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
 
EMAIL_HOST_USER = 'xxxxxxxxxxx@xxxxxxxx.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxx'
 
EMAIL_USE_TLS = True

=======
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
<<<<<<< HEAD
    ('xx', 'xxxx@pythontr.org'),
=======
    ('admin', 'admin@pythontr.org'),
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
<<<<<<< HEAD
        'NAME': DIRNAME + '/xxxxxx.db',                      # Or path to database file if using sqlite3.
=======
        'NAME': DIRNAME + '/data.db',                      # Or path to database file if using sqlite3.
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
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

<<<<<<< HEAD
MEDIA_ROOT = os.path.abspath(os.path.dirname(__file__)) + '/static_media/'
#MEDIA_ROOT = DIRNAME + '/static_media/'
#MEDIA_ROOT = '/home/electrocoder/webapps/pythontr_org/myproject/static_media'

MEDIA_URL = '/media/'
#MEDIA_URL = 'http://pythontr.org/media/'
=======

MEDIA_ROOT = DIRNAME + '/static_media/'
#MEDIA_ROOT = '/home/electrocoder/webapps/pythontr_org/myproject/static_media'

MEDIA_URL = 'http://pythontr.org/media/'
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60

STATIC_ROOT = DIRNAME + '/static/'

STATIC_URL = 'http://pythontr.org/static/'

ADMIN_MEDIA_PREFIX = 'http://pythontr.org/media/admin/'

STATICFILES_DIRS = (
    DIRNAME + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

<<<<<<< HEAD
SECRET_KEY = '8!xvqpxxxxxxxxxxxxxxxxxxxxxi&k0cxxxxxxx@ru)v'
=======
SECRET_KEY = '8!xvqp_o(er345zw$!ns0h33f=awdk=47ii&k0c@ru)v'
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60

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

#TEMPLATE_DIRS = ("/home/electrocoder/webapps/pythontr_org/myproject/templates")
<<<<<<< HEAD
TEMPLATE_DIRS = ("/home/electrocoder/workspace/pythontr_org/pythontr_org/myproject/templates")

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

DISQUS_API_KEY = 'xxxxxxI5vs3OBzK5jyKneHxxxxxxxiWgdzH1IxSLlxoos2JpnY' 
=======
TEMPLATE_DIRS = ("/home/electrocoder/virtual-python/workspace/django-python/pythontr_org/myproject/templates")

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

DISQUS_API_KEY = '7hoAnpay9gNr8s7hSI5v2341E3jUsgRiWgdzH122ISLlxoos2JpnY' 
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
DISQUS_WEBSITE_SHORTNAME = 'pythonprogramcilari'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'disqus',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'myproject.polls',
    'django.contrib.sitemaps',
    'myproject.python',
    'myproject.pythoncoders',
<<<<<<< HEAD
    'myproject.pythonauthors',
=======
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
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
