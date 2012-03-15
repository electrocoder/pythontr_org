# -*- coding: utf-8 -*-

from pythontr_org.posts.models import Post, Category


from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls.defaults import patterns


post_dict = {
    'queryset': Post.objects.filter(published = True),
    'date_field': 'created_at',
}

category_dict = {
    'queryset': Category.objects.all(),
}


sitemaps = {
    'flatpages': FlatPageSitemap,
    
    'posts': GenericSitemap(post_dict, priority=0.5),
    'categories': GenericSitemap(category_dict, priority=1),
}

SITEMAPS_URLS = patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)