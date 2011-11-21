# -*- coding:utf-8 -*-
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from myproject.python.models import Posts, Categories

class LatestPosts(Feed):
    title = ">>> Python Programcıları >>> Son yazılanlar"
    link = "/"
    description = ">>> Son 5 makale..."

    def items(self):
        return Posts.objects.filter(post_publish=True).order_by("-post_pubdate")[:5]

    def item_title(self,item):
        return ">>> " + item.post_title

    def item_description(self,item):
        return item.post_body
    
    def item_pubdate(self,item):
        return item.post_pubdate
