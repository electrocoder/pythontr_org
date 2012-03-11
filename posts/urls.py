# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pythontr_org.posts.views',
                       # gönderiler için;
                       
                       url(r'^$', 'index', name = 'index'),
                       url(r'^(?P<id>\d+)-(?P<slug>[^/]*)/$', 'show', name = 'show'),
                       url(r'^search/$', 'search', name = 'search'),
                       
                       # kategoriler için;
                       
                       url(r'^category/(?P<id>\d+)-(?P<slug>[^/]*)/$', 'category_show', name = 'show_category'),
)