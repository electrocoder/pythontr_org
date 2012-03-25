# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages

from pythontr_org.posts.models import Post, Category
from pythontr_org.posts.forms import PostForm

from pythontr_org.utils import PostListView, PostSearchListView, CategoryPostListView,\
                                MyPostListView


index = PostListView.as_view()
search = PostSearchListView.as_view()
category_show = CategoryPostListView.as_view()
my_posts = MyPostListView.as_view()


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
    