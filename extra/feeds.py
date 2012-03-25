# -*- coding:utf-8 -*-

from django.contrib.syndication.views import Feed
from django.conf.urls.defaults import patterns, url

from django.shortcuts import get_object_or_404

from pythontr_org.posts.models import Post, Category
from pythontr_org.links.models import Link
from pythontr_org.polls.models import Poll


class LatestCommunityPosts(Feed):
    """
        topluluk haber beslemesi
    """
    
    title = ">>> Python Programcıları >>> Topluluk Haberleri -- Son yazılanlar"
    link = "/"
    description = ">>> Son 5 makale..."


    def items(self):
        return Post.objects.published().filter(tags__icontains = 'topluluk')[:5]


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
        return Post.objects.published()[:5]


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
    link = '/links/'
    description = 'Python programcıları derneği son gönderilen 5 bağlantı'
    
    
    def items(self):
        return Link.objects.confirmed()[:5]
    
    
    def item_title(self, item):
        return item.title
    
    
    def item_description(self, item):
        return item.description or item.title
    
    
    def item_pubdate(self, item):
        return item.created_at


class LatestPolls(Feed):
    """
        Anketler için RSS beslemesi
    """
    
    title = 'Son açılan anketler'
    link = '/polls/'
    description = 'Python programcıları derneği son açılan 5 anket'
    
    
    def items(self):
        return Poll.objects.all()[:5]
    
    
    def item_title(self, item):
        return item.question
    
    
    def item_description(self, item):
        return item.question
    
    
    def item_pubdate(self, item):
        return item.created_at 


# urls

RSS_URLS = patterns('',
                    url(r'^rss/$', LatestPosts()),
                    url(r'^rss/community/$', LatestCommunityPosts()),
                    url(r'^rss/posts/$', LatestPosts()),
                    url(r'^rss/links/$', LatestLinks()),
                    url(r'^rss/polls/$', LatestPolls()),
)