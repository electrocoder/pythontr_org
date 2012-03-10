# -*- coding:utf-8 -*-

from django.contrib.syndication.views import Feed
from django.conf.urls.defaults import patterns

from django.shortcuts import get_object_or_404
from pythontr_org.posts.models import Post, Category

class LatestCommunityPosts(Feed):
    """
    topluluk haber beslemesi
    """
    
    title = ">>> Python Programcıları >>> Topluluk Haberleri -- Son yazılanlar"
    link = "/"
    description = ">>> Son 5 makale..."

    def items(self):
        return Post.objects.filter(tags__contains = 'topluluk')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
    
    def item_pubdate(self, item):
        return item.created_at


class LatestPosts(Feed):
    """
    blog haber beslemesi
    """
    
    title = ">>> Python Programcıları >>> Blog Haberleri -- Son yazılanlar"
    link = "/"
    description = ">>> Son 5 makale..."

    def items(self):
        return Post.objects.filter(published=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
    
    def item_pubdate(self, item):
        return item.created_at


# urls

RSS_URLS = patterns('',
                    (r'^rss/$', LatestPosts()),
                    (r'^rss/topluluk/$', LatestCommunityPosts()),
                    (r'^rss/blog/$', LatestPosts()),
)