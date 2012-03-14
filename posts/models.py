# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.sitemaps import ping_google

from django.core.exceptions import ValidationError

from pythontr_org.slughifi import slughifi

def validate_user_is_in_authors_group(value):
    """
        Gönderiyi ekleyen üyenin
        yazar olup olmadığını kontrol eder.
        
        Yazar değilse uyarı verir.
    """
    
    user = User.objects.get(id = value)
    group = Group.objects.get(name = 'Yazarlar')
    if not user in group.user_set.all():
        raise ValidationError(u'%s adlı kullanıcı bir yazar değil.' % user.username)
        


class Category(models.Model):
    """
        Kategorileri depolamak için kullanılan model.
        'name' alanını içerir.
    """
    
    name = models.CharField("Adı", unique=True, max_length=50)
    slug = models.SlugField('Slug', max_length = 255, blank = True, null = True)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('posts:show_category', [self.pk, self.slug]) 

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

class Post(models.Model):
    """
        Gönderileri depolamak için yapılmış model.
        
        Gerekli olan alanlar;
            author, title, category, slug, content, published, tags
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
    
    slug = models.SlugField(
                            "URL için uygun hali",
    )
    
    content = models.TextField(
                               "Gönderinin içeriği",
                               help_text = 'Bu alanda Textile işaretleme dili kullanabilirsiniz.',
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
        
        if not self.id:
            self.slug = slughifi(self.title)
        
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

    def get_tags_as_list(self):
        tags = []
        for tag in self.tags.split(','):
            tags.append(tag.strip())
        
        return tags
    
         
    class Meta:
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        
        ordering = ['-created_at']

