# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pythontr_org.posts.views',
                       # gönderiler için;
                       
                       url(r'^$', 'index', name = 'index'),
                       url(r'^(?P<id>\d+)-(?P<slug>[^/]*)/$', 'show', name = 'show'),
                       
                       # kategoriler için;
                       
                       url(r'^categories/$', 'category_index', name = 'index_category'),
                       url(r'^category/(?P<id>\d+)/$', 'category_show', name = 'show_category'),
)