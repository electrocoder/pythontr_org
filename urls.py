# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.conf import settings
from django.contrib import admin

from django.conf.urls.defaults import *


# STATIC ve MEDIA dosyaları için
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pythontr_org.feeds import RSS_URLS
from pythontr_org.sitemaps import SITEMAPS_URLS

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^errors/access_denied/$', 'pythontr_org.extra.views.access_denied', name = 'access_denied'),
                       
                       url(r'^contact/$', 'pythontr_org.extra.views.contact', name = 'contact'),
                       
                       url(r'^posts/', include('pythontr_org.posts.urls', namespace = 'posts')),
    
                       url(r'^polls/', include('pythontr_org.polls.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),   
                       url(r'^accounts/', include('pythontr_org.users.urls', namespace = 'users')),                    
)

urlpatterns += SITEMAPS_URLS 
urlpatterns += RSS_URLS

# static ve media klasörlerini sun.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
