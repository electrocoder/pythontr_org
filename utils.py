# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list


def posts_object_list(request, queryset, template_name, *args, **kwargs):    
    return object_list(
                           request,
                           queryset,
                           paginate_by=15,
                           template_name='posts/%s' % template_name,
                           template_object_name='posts',
                           *args,
                           **kwargs
                       )
    
    
def links_object_list(request, queryset, template_name, *args, **kwargs):
    return object_list(
                            request,
                            queryset,
                            paginate_by=15,
                            template_name='links/%s' % template_name,
                            template_object_name='links',
                            *args,
                            **kwargs
                       )    