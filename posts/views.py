# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, get_list_or_404


from pythontr_org.posts.models import Post, Author, Category


# Gönderiler için

def index(request):
    """
        Gönderileri listeler.
    """
    
    posts = Post.objects.all()
    
    return render(request, 'posts/index.html', locals())

def show(request, id, slug):
    """
        Gönderiyi göstermek için kullanılır.
        Eğer gönderi bulunamazsa 404 döndürür.
    """
    
    post = get_object_or_404(Post, pk = id)
    
    return render(request, 'posts/show.html', locals())



# Kategoriler için

def category_index(request):
    """
        Kategorileri listeler.
    """
    
    categories = Category.objects.all()
    
    return render(request, 'posts/category_index.html', locals())

def category_show(request, id):
    """
        Bu kategoriye bağlı gönderileri bulmak için kullanılır.
        Eğer kategori bulunmazsa 404 döndürür.
    """
    
    category = get_object_or_404(Category, pk = id)
    
    return render(request, 'posts/category_show.html', locals())
