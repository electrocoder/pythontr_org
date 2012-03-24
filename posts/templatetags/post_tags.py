# -*- coding: utf-8 -*-

from django import template

from pythontr_org.posts.models import Post, Category

register = template.Library()


# Sol menüde yer alan;
#    Kategoriler
#    Son gönderilenler
#    En çok okunanlar
#
# için template tagları


@register.inclusion_tag('posts/templatetags/_posts.html')
def get_five_latest_posts():
    """
        Son beş gönderiyi listeler.
    """    
    return {'p_list': Post.objects.filter(published = True)[:5]}


@register.inclusion_tag('posts/templatetags/_posts.html')
def get_five_most_reads():
    """
        En çok okunan beş gönderiyi listeler.
    """
    return {'p_list': Post.objects.filter(published = True).order_by('-read_count')[:5]}


@register.inclusion_tag('posts/templatetags/_categories.html')
def get_categories():
    """
        Kategorileri listeler.
    """
    return {'c_list': Category.objects.all()}