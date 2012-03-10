# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google

class Category(models.Model):
    """
        Kategorileri depolamak için kullanılan model.
        'name' alanını içerir.
    """
    
    name = models.CharField("Adı", unique=True, max_length=50)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('posts:show_category', [self.pk]) 

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    
class Author(models.Model):
    """
        Yazar alanını depolamak için kullanılan model.
        'user', 'photo', 'web_site', 'bio' alanlarını içerir.
        
        'user' alanı django.contrib.auth.models.User modeli ile bire-bir ilişkilir.
        
        Gerekli alanlar;
            'user', ayrıca benzersiz olması gerekir.
    
    """
    
    user = models.OneToOneField(User, verbose_name = "Üye", unique=True)
    
    photo = models.ImageField(
                              upload_to = 'user-images',
                              verbose_name = "Resim",
                              help_text ='Sadece BMP, GIF veya PNG formatında resim kullanılabilir.',
                              null = True, blank = True
    )
    
    web_site = models.CharField(
                                max_length = 255,
                                verbose_name = "Web sitesi",
                                help_text = "Yazarın web adresi.",
                                blank = True, null = True
    )
    
    about = models.TextField(verbose_name = "Yazar hakkında kısa açıklama.", blank = True, null = True)

    def __unicode__(self):
        return self.user.username
        
    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"


class Post(models.Model):
    """
        Gönderileri depolamak için yapılmış model.
        
        Gerekli olan alanlar;
            author, title, category, slug, content, published, tags
    """
    
    author = models.ForeignKey(
                               Author,
                               verbose_name = "Yazar",
                               help_text = "Gönderin yazarı.",
                               )
    
    title = models.CharField(
                             "Başlık",
                             help_text = "Gönderinin başlığı",
                             max_length=255
    )
    
    category = models.ForeignKey(Category, verbose_name = "Kategori")
    
    slug = models.SlugField(
                            "URL için uygun hali",
    )
    
    content = models.TextField(
                               "Gönderinin içeriği",
                               help_text = 'Bu alanda HTML kullanabilirsiniz.',
    )
    
    published = models.BooleanField(
                                    "Yayınlasın mı?",
                                    default=True,
                                    help_text = "Bu alan gönderinin yayınlanıp yayınlanmayacağını belirler."
    )
    
    tags = models.CharField("Etiket(ler)", max_length=100, help_text = "Virgül (,) ile birbirlerinden ayırabilirsiniz.")
    read_count = models.IntegerField("Okunma sayısı", default=0)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('posts:show', [self.pk, self.slug])
    
    def save(self, force_insert=False, force_update=False):
        super(Post, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass
             
    class Meta:
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        
        ordering = ['-created_at']

