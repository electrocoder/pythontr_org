# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth.models import Group, User

from pythontr_org.links.models import Link
from pythontr_org.posts.models import Post, Category
from pythontr_org.polls.models import Poll, Vote, Choice


class PermissionProtectedView(object):
    @method_decorator(permission_required('posts.add_post'))
    def dispatch(self, *args, **kwargs):
        return super(PermissionProtectedView, self).dispatch(*args, **kwargs)


class ProtectedView(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


class SettingsView(ProtectedView, TemplateView):
    template_name='users/settings.html'
    

class MainListView(ListView):
    paginate_by = 20



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
        return Post.objects.search(self.request.GET.get('q', ''))
    
    
    def get_context_data(self, **kwargs):
        context = super(PostSearchListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        
        return context

    
class CategoryPostListView(PostListView):
    template_name='posts/category_show.html'
    
    def get_queryset(self):
        self.category=get_object_or_404(Category, slug=self.kwargs['slug'])
        
        return self.category.post_set.filter(published=True)
    
    
    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        
        return context


class MyPostListView(PermissionProtectedView, PostListView):
    template_name='posts/my_posts.html'
    paginate_by=6
    
    
    def get_queryset(self):
        return self.request.user.post_set.all()
    
    
class UserPostListView(PostListView):
    paginate_by=6
    template_name='users/profile.html'
    
    def get_queryset(self):
        self.tuser = get_object_or_404(User, username=self.kwargs['username'])
        self.profile = self.tuser.get_profile()
        
        self.is_me = self.tuser.username == self.request.user
        self.group = Group.objects.get(name='Yazarlar')
        
        if self.group.user_set.filter(username = self.tuser):
            return self.tuser.post_set.filter(published=True)
        else:
            return []
        
    
    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        
        context.update({
                            'is_me': self.is_me,
                            'group': self.group,
                            'profile': self.profile,
                            'tuser': self.tuser,
                        }) 
        
        return context