from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from myproject.python.models import Posts, Authors, Categories
from sitemaps import PostsSitemap, CategoriesSitemap
from feeds import LatestPosts, LatestPostsBlog
from myproject.pythoncoders.models import PythonCoders
from myproject.pythonauthors.models import PythonAuthors

admin.autodiscover()

import os.path
DIRNAME = os.path.dirname(__file__)

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
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "static/")}),    
    (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, settings.MEDIA_ROOT)}),    

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

urlpatterns += patterns('',
    (r'^rss/$', LatestPosts()),
    (r'^rss/topluluk/$', LatestPosts()),
    (r'^rss/blog/$', LatestPostsBlog()),
)
