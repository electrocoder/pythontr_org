# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from pythontr_org.posts.models import Post, Category
from pythontr_org.posts.forms import PostForm

# Gönderiler için

def index(request):
    """
        Gönderileri listeler.
    """
    
    posts = Post.objects.filter(published = True)
    
    return render(request, 'posts/index.html', locals())

def show(request, id, slug):
    """
        Gönderiyi göstermek için kullanılır.
        Eğer gönderi bulunamazsa 404 döndürür.
    """
    
    post = get_object_or_404(Post, pk = id, published = True)
    post.increase_read_count()
    
    return render(request, 'posts/show.html', locals())

def search(request):
    """
        Gönderileri aramak için kullanılır.
        Aranan yapı Post modelinin 'content' alında bulunuyorsa seçer.
    """
    q = request.GET.get('q', '')
    
    posts = Post.objects.filter(content__icontains = q)
    
    return render(request, 'posts/search.html', locals())    

# Kategoriler ile ilgili.

def category_show(request, id, slug):
    """
        Bu kategoriye bağlı gönderileri bulmak için kullanılır.
        Eğer kategori bulunmazsa 404 döndürür.
    """
    
    category = get_object_or_404(Category, pk = id)
    posts = category.post_set.all()
    
    return render(request, 'posts/category_show.html', locals())


# yeni gönderi ekleme, düzenleme ve silme

@login_required
def new(request):
    """
        Yeni gönderi eklemek için kullanılır.
    """
    
    if request.method == 'POST':
        post = Post(author = request.user, published = False)
        
        form = PostForm(request.POST, instance = post)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Gönderi başarı ile eklendi.')
            return redirect('posts:index')
    else:
        form = PostForm()