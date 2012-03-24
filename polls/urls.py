# -*- coding: utf-8-*-

from django.conf.urls.defaults import *

urlpatterns = patterns('pythontr_org.polls.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<slug>[^/]*)/$', 'detail', name='detail'),
    url(r'^(?P<slug>[^/]*)/results/$', 'results', name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),
)
