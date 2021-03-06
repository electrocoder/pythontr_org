# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

from pythontr_org.links.views import LinkListView, NewLinkView

urlpatterns = patterns('pythontr_org.links.views',
                       url(r'^$', LinkListView.as_view(), name='index'),
                       url(r'^new/$', NewLinkView.as_view(), name='new')
)