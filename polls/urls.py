# -*- coding: utf-8-*-

from django.conf.urls.defaults import url, patterns

from pythontr_org.polls.views import PollListView, PollDetailView

urlpatterns = patterns('pythontr_org.polls.views',
    url(r'^$', PollListView.as_view(), name='index'),
    url(r'^(?P<slug>[^/]*)/$', PollDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[^/]*)/results/$', PollDetailView.as_view(), name='results'),
    url(r'^(?P<slug>[^/]*)/vote/$', 'vote', name='vote'),
)