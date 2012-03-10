# -*- coding: utf-8-*-

from django.conf.urls.defaults import *

urlpatterns = patterns('pythontr_org.polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
