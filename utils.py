# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list


def post_list(request, queryset, template_name, *args, **kwargs):    
    return object_list(
                           request,
                           queryset,
                           paginate_by=15,
                           template_name='posts/%s' % template_name,
                           template_object_name='post',
                           *args,
                           **kwargs
                       )
    
    
def link_list(request, queryset, template_name, *args, **kwargs):
    return object_list(
                            request,
                            queryset,
                            paginate_by=15,
                            template_name='links/%s' % template_name,
                            template_object_name='link',
                            *args,
                            **kwargs
                       )


def user_post_list(request, queryset, *args, **kwargs):
    return object_list(
                       request,
                       queryset,
                       paginate_by=10,
                       template_name='users/profile.html',
                       template_object_name='post',
                       *args,
                       **kwargs
                       )