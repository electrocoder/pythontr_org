# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list_detail import object_list


from pythontr_org.posts.models import Post

posts_info = {
              'queryset': Post.objects.filter(published = True),
              'paginate_by': 30,
              'template_name': 'posts/index.html',
}

urlpatterns = patterns('pythontr_org.posts.views',
                       # gönderiler için;
                       
                       url(r'^$', object_list, posts_info, name = 'index'),
                       
                       url(r'^detail/(?P<category_slug>[^/]*)/(?P<slug>[^/]*)/$', 'show', name = 'show'),
                       url(r'^search/$', 'search', name = 'search'),
                       
                       # kategoriler için;
                       
                       url(r'^category/(?P<slug>[^/]*)/$', 'category_show', name = 'show_category'),
                       
                       url(r'^new/$', 'new', name = 'new'),
                       url(r'^(?P<id>\d+)/edit/$', 'edit', name = 'edit'),
                       url(r'^(?P<id>\d+)/delete/$', 'delete', name = 'delete'),
                       
                       
                       url(r'^my_posts/$', 'my_posts', name = 'my_posts'),
)