# -*- coding:utf-8 -*-
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from myproject.python.models import Posts, Categories

class LatestPosts(Feed):
<<<<<<< HEAD
    """
    topluluk haber beslemesi
    """
    title = ">>> Python Programcıları >>> Topluluk Haberleri -- Son yazılanlar"
    link = "/"
    description = ">>> Son 5 makale..."

    def items(self):
        #return Posts.objects.filter(post_publish=True).order_by("-post_pubdate")[:5]
        return Posts.objects.filter(post_tags = 'topluluk').order_by("-post_pubdate")[:5]

    def item_title(self,item):
        return ">>> " + item.post_title

    def item_description(self,item):
        return item.post_body
    
    def item_pubdate(self,item):
        return item.post_pubdate
    
class LatestPostsBlog(Feed):
    """
    blog haber beslemesi
    """
    title = ">>> Python Programcıları >>> Blog Haberleri -- Son yazılanlar"
=======
    title = ">>> Python Programcıları >>> Son yazılanlar"
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
    link = "/"
    description = ">>> Son 5 makale..."

    def items(self):
        return Posts.objects.filter(post_publish=True).order_by("-post_pubdate")[:5]
<<<<<<< HEAD
        #return Posts.objects.filter(post_tags != 'topluluk').order_by("-post_pubdate")[:5]
=======
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60

    def item_title(self,item):
        return ">>> " + item.post_title

    def item_description(self,item):
        return item.post_body
    
    def item_pubdate(self,item):
        return item.post_pubdate
