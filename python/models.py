from django.db import models
from datetime import datetime
from django.core.files import File
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google

class Categories(models.Model):
    category_name = models.CharField("Kategori", unique=True, max_length=50)
    
    def __unicode__(self):
        return self.category_name

    def get_absolute_url(self):
        return "/python/" + self.category_name 

    class Meta:
        verbose_name_plural = "Kategoriler"
    
class Authors(models.Model):
    author_name = models.OneToOneField(User, verbose_name = "Isim", unique=True)
    author_photo = models.ImageField(upload_to = 'user-images', verbose_name = "Resim", help_text ='*.gif veya *.bmp', null = True, blank = True)
    author_web = models.CharField(max_length = 75, verbose_name = "Web sitesi", blank = True, null = True)
    author_email = models.EmailField(verbose_name = "E-mail")
    author_bio = models.TextField(verbose_name = "Kisa aciklama", blank = True, null = True)

    def __unicode__(self):
        return self.author_name.username
        
    class Meta:
        verbose_name_plural = "Yazarlar"
        
class Posts(models.Model):
    post_author = models.ForeignKey(Authors, verbose_name = "Yazar")
    post_title = models.CharField("Baslik", max_length=150)
    post_link = models.SlugField("Kisa link")
    post_body = models.TextField("Icerik", help_text = 'Bu alanda HTML kullanabilirsiniz.')
    post_category = models.ForeignKey(Categories, verbose_name = "Kategori")
    post_pubdate = models.DateTimeField("Yayin tarihi", default = datetime.now)
    post_update = models.DateTimeField("Guncelleme tarihi",  default = datetime.now)
    post_publish = models.BooleanField("Yayinlansinmi?", default=True)
    post_tags = models.TextField("Etiket(ler)", max_length=20)
    post_read_count = models.IntegerField("Okunma sayisi", default=0)
    post_star = models.IntegerField("Begenilme sayisi", default=1)
    
    def __unicode__(self):
        return self.post_title

    def get_absolute_url(self):
        return "/python/" + self.post_category.category_name + "/" + self.post_link
    
    def save(self, force_insert=False, force_update=False):
        super(Posts, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass
             
    class Meta:
        verbose_name_plural = "Gonderiler"

