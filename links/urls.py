# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pythontr_org.links.views',
                       url(r'^$', 'index', name = 'index'),
                       url(r'^new/$', 'new', name = 'new'),
)