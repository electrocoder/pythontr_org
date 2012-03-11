# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, get_list_or_404

from pythontr_org.posts.models import Post, Category


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