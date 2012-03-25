# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView

from django.contrib.auth.models import Group, User

from pythontr_org.links.models import Link
from pythontr_org.posts.models import Post, Category
from pythontr_org.polls.models import Poll, Vote, Choice


class MainListView(ListView):
    paginate_by = 15



class AuthorListView(ListView):
    template_name='users/authors.html'
    paginate_by=4
    
    template_object_name='user'
    
    group=get_object_or_404(Group, name='Yazarlar')
    queryset=group.user_set.filter(is_active=True)


class LinkListView(MainListView):
    template_name='links/index.html'
    
    queryset=Link.objects.confirmed()
    template_object_name='link_list'


class PollListView(MainListView):
    template_name = 'polls/index.html'    
    model = Poll


class PollDetailView(DetailView):
    template_name = 'polls/detail.html'
    model = Poll
        
    def get_context_data(self, **kwargs):
       context = super(PollDetailView, self).get_context_data(**kwargs)
       
       try:
           vote = Vote.objects.get(user=self.request.user, poll=get_object_or_404(Poll, slug=self.kwargs['slug']))
           context['vote'] = vote
       except:
           pass
       
       return context


class PostListView(MainListView):
    queryset=Post.objects.published()
    template_name='posts/index.html'
    template_object_name='post'


class PostSearchListView(PostListView):
    template_name='posts/search.html'
    
    def get_queryset(self):
        return Post.objects.published().filter(content__icontains=self.request.GET.get('q', ''))
    
    def get_context_data(self, **kwargs):
        context = super(PostSearchListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        
        return context

    
class CategoryPostListView(MainListView):
    template_name='posts/category_show.html'
    
    def get_queryset(self):
        self.category=get_object_or_404(Category, slug=self.kwargs['slug'])
        return self.category.post_set.published()
    
    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        
        return context


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