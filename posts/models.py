# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, Group

from django.contrib.sitemaps import ping_google
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from pythontr_org.utils import slugify_unicode


GOOGLE_CODE_PRETTIFY = (u'''
    <a href='http://google-code-prettify.googlecode.com/svn/trunk/README.html' target='_blank'>
        Kod renklendirme için tıklayınız.
    </a>
''')


class Category(models.Model):
    """
        Kategorileri depolamak için kullanılan model.
        'name' alanını içerir.
    """
    
    name = models.CharField("Adı", unique=True, max_length=50)
    slug = models.SlugField('Slug', max_length = 255, blank = True, null = True)
    
    image = models.ImageField(upload_to='category_images')
    
    def __unicode__(self):
        return self.name
    
    
    @models.permalink
    def get_absolute_url(self):
        return ('posts:show_category', [self.slug]) 
    
    
    class Meta:
        verbose_name        = "Kategori"
        verbose_name_plural = "Kategoriler"
        
        ordering = ['name']


def validate_user_is_in_authors_group(value):
    """
        Gönderiyi ekleyen üyenin
        yazar olup olmadığını kontrol eder.
        
        Yazar değilse uyarı verir.
    """
    
    user  = User.objects.get(id = value)
    group = Group.objects.get(name = 'Yazarlar')
    
    if not user in group.user_set.all():
        raise ValidationError(u'%s adlı kullanıcı bir yazar değil.' % user.username)
        

class PostManager(models.Manager):
    def published(self):
        return Post.objects.filter(published=True)
    
    
    def search(self, q):
        return Post.objects.published().filter(content__icontains=q)


class Post(models.Model):
    """
        Gönderileri depolamak için yapılmış model.
        
        'short_title': 35 karaktere kadar başlığı yazar
        ondan sonra '...' koyar.
        
        'short_content': 125 karaktere kadar içeriği yazar
        ondan sonra '...' koyar.
        
        'increase_read_count': Okunma sayısını 1 arttırır.
    """
    
    
    author = models.ForeignKey(
                               User,
                               verbose_name = "Yazar",
                               help_text = "Gönderin yazarı.",
                               validators = [validate_user_is_in_authors_group]
                               )
    
    title = models.CharField(
                             "Başlık",
                             help_text = "Gönderinin başlığı",
                             max_length=255
    )
    
    category = models.ForeignKey(Category, verbose_name = "Kategori")
    
    slug = models.SlugField("URL için uygun hali")
    
    content = models.TextField(
                               "Gönderinin içeriği",
                               help_text = mark_safe('Bu alanda HTML kullanabilirsiniz. ' + GOOGLE_CODE_PRETTIFY),
    )
    
    published = models.BooleanField(
                                    "Yayınlasın mı?",
                                    default=True,
                                    help_text = "Bu alan gönderinin yayınlanıp yayınlanmayacağını belirler."
    )
    
    tags = models.CharField("Etiket(ler)", max_length=100, help_text = "Virgül (,) ile birbirlerinden ayırabilirsiniz.",
                            blank = True, null = True
                            )
    read_count = models.IntegerField("Okunma sayısı", default=0)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    objects= PostManager()
    
    def __unicode__(self):
        return self.title
    

    @models.permalink
    def get_absolute_url(self):
        return ('posts:show', [self.category.slug, self.slug])
    
    
    def save(self, force_insert=False, force_update=False):
        
        if not self.id:
            self.slug = slugify_unicode(u"%s" % self.title)
        
        super(Post, self).save(force_insert, force_update)
        
        try:
            ping_google()
        except Exception:
            pass
    
         
    def short_title(self):
        if len(self.title) > 34:
            return self.title[:35] + '...'
        else:
            return self.title
     
    def short_content(self):
        if len(self.content) > 124:
            return self.content[:125] + '...'
        else:
            return self.content 

    def increase_read_count(self):
        self.read_count += 1
        self.save()
         
    class Meta:
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        
        ordering = ['-created_at']
        get_latest_by = 'created_at'