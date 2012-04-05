# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages
from django.views.generic import ListView, CreateView

from pythontr_org.posts.models import Post, Category
from pythontr_org.posts.forms import PostForm

from pythontr_org.utils import ProtectedView


class PostListView(ListView):
    queryset=Post.objects.published()
    paginate_by=20
    
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


class CategoryListView(ListView):
    model      =  Category
    paginate_by = 16
    
    template_name        = 'posts/categories.html'
    template_object_name = 'category_list'


class MyPostListView(PostListView, ProtectedView):
    template_name='posts/my_posts.html'
    paginate_by=6
    
    
    def get_queryset(self):
        return self.request.user.post_set.all()
    

def show(request, category_slug, slug):
    """
        Gönderiyi göstermek için kullanılır.
        Eğer gönderi bulunamazsa 404 döndürür.
    """
    
    post = get_object_or_404(Post, slug = slug, published = True, category__slug = category_slug)
    post.increase_read_count()
    
    return render(request, 'posts/show.html', locals())


# yeni gönderi ekleme, düzenleme ve silme

@permission_required('posts.add_post')
def new(request):
    """
        Yeni gönderi eklemek için kullanılır.
    """
    
    
    post = Post(author = request.user)
    
    form = PostForm(request.POST or None, instance = post)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, u'Gönderi başarı ile eklendi.')
        return redirect('posts:my_posts')    
        

    return render(request, 'posts/new.html', locals())


class NewPostView(CreateView):
    template_name = 'posts/new.html'
    #form_class = PostForm
    
    def get_form_class(self):
        post = Post(author = self.request.user)
        
        return PostForm(instance=post)
    

@permission_required('posts.change_post')
def edit(request, id):
    """
        Gönderiyi düzenlemek için kullanılır.
    """
    
    post = get_object_or_404(Post, id = id)
    
    # eğer request.user gönderinin sahibi değilse
    # erişim engellendi sayfasına yönlendir.
    
    if not post.author == request.user:
        return redirect('access_denied')
    
    form = PostForm(request.POST or None, instance = post)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, u'Gönderi başarı ile düzenlendi.')
        
        return redirect('posts:my_posts')
    
        
    return render(request, 'posts/edit.html', locals())

    
@permission_required('posts.delete_post')
def delete(request, id):
    """
        Gönderi silmek için kullanılır.
    """
    
    post = get_object_or_404(Post, id = id)
    
    if not request.user == post.author:
        return redirect('access_denied')
    
    post.delete()
    
    messages.success(request, u'"%s" başlıklı gönderi başarı ile silindi' % post.title)
    
    return redirect('posts:my_posts')
    