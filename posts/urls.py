# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pythontr_org.posts.views',
                       # gönderiler için;
                       
                       url(r'^$', 'index', name = 'index'),                       
                       url(r'^posts/new/$', 'new', name = 'new'),
                       url(r'^search/$', 'search', name = 'search'),                                             
                       url(r'^my_posts/$', 'my_posts', name = 'my_posts'),


                       url(r'^(?P<slug>[^/]*)/$', 'category_show', name = 'show_category'),
                       url(r'^(?P<category_slug>[^/]*)/(?P<slug>[^/]*)/$', 'show', name = 'show'),                       


                       url(r'^posts/(?P<id>\d+)/edit/$', 'edit', name = 'edit'),
                       url(r'^posts/(?P<id>\d+)/delete/$', 'delete', name = 'delete'),
)