#-*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class PythonAuthors(models.Model):
    """
    Amac : PythonTr de kayitlı olmayan ama Python programlama dili
    hakkında az çok bilgisi olan coderlerin iletişimi
    için gerekli olan sınıf...
    
    Tarih : 03-12-2011
    Ekleyen : sahin
    """
    #pythonauthors_name = models.OneToOneField(User, verbose_name = "Isim", unique=True)
    pythonauthors_name = models.CharField(max_length = 75, verbose_name = "Isim", unique=True)
    #pythonauthors_photo = models.ImageField(upload_to = 'user-images', verbose_name = "Resim", help_text ='*.gif veya *.bmp', null = True, blank = True)
    pythonauthors_photo = models.ImageField(upload_to = 'coderphotos', verbose_name = "Resim", help_text ='*.gif veya *.bmp', null = True, blank = True)
    pythonauthors_web = models.CharField(max_length = 75, verbose_name = "Web sitesi", blank = True, null = True)
    pythonauthors_email = models.EmailField(verbose_name = "E-mail")
    pythonauthors_content = models.TextField(verbose_name = "Kisa aciklama", blank = True, null = True)

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )
    
    def save(self, *args, **kwargs):
        self.slug = self.pythonauthors_photo.name
        super(PythonAuthors, self).save(*args, **kwargs)
            
#    def save(self):
#        for field in self._meta.fields:
#            if field.name == 'pythonauthors_photo':
#                field.upload_to = 'coderphotos/%d' % self.id
#        super(PythonCoders, self).save()

    def __unicode__(self):
        #return self.author_name.username
        return self.pythonauthors_name
        
    class Meta:
        verbose_name_plural = "Python Severler Makale"
    
    
#    class SpecialImageField(ImageField):
#        
#        def get_directory_name(self):
#            if callable(self.upload_to):
#                return self.upload_to()
#            else:
#                return super(SpecialImageField, self).get_directory_name()
