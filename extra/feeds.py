# -*- coding:utf-8 -*-

from django.contrib.syndication.views import Feed
from django.conf.urls.defaults import patterns

from django.shortcuts import get_object_or_404
from pythontr_org.posts.models import Post, Category
from pythontr_org.links.models import Link


class LatestCommunityPosts(Feed):
    """
    topluluk haber beslemesi
    """
    
    title = ">>> Python Programcıları >>> Topluluk Haberleri -- Son yazılanlar"
    link = "/"
    description = ">>> Son 5 makale..."

    def items(self):
        return Post.objects.filter(published = True, tags__icontains = 'topluluk')[:5]

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


class LatestLinks(Feed):
    """
        Bağlantı RSS beslemesi
    """
    
    title = 'Son gönderilen bağlantılar'
    link = '/'
    description = 'Python programcıları derneği son gönderilen 5 bağlantı'
    
    def items(self):
        return Link.objects.filter(confirmed = True)[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.description or item.title
    
    def item_pubdate(self, item):
        return item.created_at


# urls

RSS_URLS = patterns('',
                    (r'^rss/$', LatestPosts()),
                    (r'^rss/community/$', LatestCommunityPosts()),
                    (r'^rss/posts/$', LatestPosts()),
                    (r'^rss/links/$', LatestLinks())
)