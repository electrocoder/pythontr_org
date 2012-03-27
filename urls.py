# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

# STATIC ve MEDIA dosyaları için

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pythontr_org.main.feeds import RSS_URLS
from pythontr_org.main.sitemaps import SITEMAPS_URLS


urlpatterns = SITEMAPS_URLS 
urlpatterns += RSS_URLS


urlpatterns += patterns('',                       
                       url(r'^links/', include('pythontr_org.links.urls', namespace='links')),                                              
                       url(r'^polls/', include('pythontr_org.polls.urls', namespace='polls')),
                       
                       url(r'^accounts/', include('pythontr_org.users.urls', namespace='users')),
                       
                       url(r'^tinymce/', include('tinymce.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('pythontr_org.main.urls')),                          
                       url(r'^', include('pythontr_org.posts.urls', namespace='posts')),            
)

# static ve media klasörlerini sun.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
