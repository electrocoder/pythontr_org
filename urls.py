# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.conf import settings
from django.contrib import admin

from django.conf.urls.defaults import *
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

# STATIC ve MEDIA dosyaları için
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from pythontr_org.posts.models import Post, Author, Category
from sitemaps import PostsSitemap, CategoriesSitemap

from feeds import RSS_URLS

from pythontr_org.pythoncoders.models import PythonCoders
from pythontr_org.pythonauthors.models import PythonAuthors

admin.autodiscover()

info_dict = {
    'queryset': Posts.objects.all(),
    'date_field': 'post_pubdate',
}

info_dict_cat = {
    'queryset': Categories.objects.all(),
#    'date_field': 'post_pubdate',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(info_dict, priority=0.5),
    'categori': GenericSitemap(info_dict_cat, priority=1),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', { 'url': '/python/' }),
    (r'^/$', 'myproject.python.views.index'),
    (r'^python/$', 'myproject.python.views.index'),
    (r'^python/(?P<category>[^/]*)/$', 'myproject.python.views.category'),
    (r'^python/(?P<category>[^/]*)/(?P<link>[^/]*)/', 'myproject.python.views.show'),
    
    (r'^codebank/', 'myproject.python.views.codebank'),
        
    (r'^pythonshell/$',direct_to_template,{'template': 'pythonshell.html'}),
    (r'^iletisim/$',direct_to_template,{'template': 'iletisim.html'}),
    (r'^visual-tkinter-1/$',direct_to_template,{'template': 'visual-python-1.html'}),
    (r'^visual-python-2/$',direct_to_template,{'template': 'visual-python-2.html'}),
    (r'^bagisyap/$',direct_to_template,{'template': 'bagisyap.html'}),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')), 
    (r'^admin/', include(admin.site.urls)),
    
    (r'^polls/', include('myproject.polls.urls')),
    (r'^pythoncoders/$', 'myproject.pythoncoders.views.contact'),
    (r'^python-programcilari-liste/$', 'myproject.pythoncoders.views.list'),

    (r'^pythonauthors/$', 'myproject.pythonauthors.views.contact'),

)

urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)

# rss 

urlpatterns += RSS_URLS

# static ve media klasörlerini sun.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
