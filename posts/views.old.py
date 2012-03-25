#def search(request):
#    """
#        Gönderileri aramak için kullanılır.
#        Aranan yapı Post modelinin 'content' alında bulunuyorsa seçer.
#    """
#    
#    q = request.GET.get('q', '')
#    return post_list(request,
#                       queryset=Post.objects.published().filter(content__icontains = q), 
#                       template_name='search.html',
#                       extra_context=locals(),
#                       )


# Kategoriler ile ilgili.

#def category_show(request, slug):
#    """
#        Bu kategoriye bağlı gönderileri bulmak için kullanılır.
#        Eğer kategori bulunmazsa 404 döndürür.
#    """
#    
#    category = get_object_or_404(Category, slug = slug)    
#    return post_list(request,
#                       queryset=category.post_set.published(),
#                       template_name='category_show.html',
#                       extra_context=locals(),
#                       )


#@permission_required('posts.add_post')
#def my_posts(request):
#    """
#        Yazarın kendi gönderdiği gönderilerin listelendiği
#        düzenle ve sil bağlantılarının yer aldığı sayfa.
#    """
#    return post_list(request, request.user.post_set.all(),'my_posts.html')
    