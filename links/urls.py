# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

from pythontr_org.links.views import LinkListView

urlpatterns = patterns('pythontr_org.links.views',
                       url(r'^$', LinkListView.as_view(), name='index'),
                       url(r'^new/$', 'new', name='new'),
)