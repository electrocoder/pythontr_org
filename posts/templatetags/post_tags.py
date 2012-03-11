# -*- coding: utf-8 -*-

from django import template

from pythontr_org.posts.models import Post, Category

register = template.Library()

@register.inclusion_tag('posts/_posts.html')
def get_five_latest_posts():
    """
        Son beş gönderiyi listeler.
    """
    
    posts = Post.objects.filter(published = True)[:5]
    
    return {'posts_list': posts}

@register.inclusion_tag('posts/_posts.html')
def get_most_reads():
    """
        En çok okunan 5 gönderiyi listeler.
    """
    
    posts = Post.objects.filter(published = True).order_by('-read_count')[:5]
    
    return {'posts_list': posts}

@register.inclusion_tag('posts/_categories.html')
def get_categories():
    """
        Kategorileri listeler.
    """
    
    categories = Category.objects.all()
    
    return {'categories_list': categories}