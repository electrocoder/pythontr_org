#-*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User

class PythonCoders(models.Model):
    """
    Amac : PythonTr de kayitlı olmayan ama Python programlama dili
    hakkında az çok bilgisi olan coderlerin iletişimi
    için gerekli olan sınıf...
    
    Tarih : 03-12-2011
    Ekleyen : sahin
    """
    pythoncoders_name = models.OneToOneField(User, verbose_name = "Isim", unique=True)
    #pythoncoders_photo = models.ImageField(upload_to = 'user-images', verbose_name = "Resim", help_text ='*.gif veya *.bmp', null = True, blank = True)
    pythoncoders_photo = models.ImageField(upload_to='coderphotos')
    pythoncoders_web = models.CharField(max_length = 75, verbose_name = "Web sitesi", blank = True, null = True)
    pythoncoders_email = models.EmailField(verbose_name = "E-mail")
    pythoncoders_bio = models.TextField(verbose_name = "Kisa aciklama", blank = True, null = True)
    pythoncoders_git = models.CharField(max_length = 75, verbose_name = "Git adresi", blank = True, null = True)
    pythoncoders_mobil = models.CharField(max_length = 11, verbose_name = "Cep Telefonu", blank = True, null = True)
    pythoncoders_star = models.CharField(max_length = 11, verbose_name = "Python bilgisi", blank = True, null = True)
    
    def save(self):
        for field in self._meta.fields:
            if field.name == 'pythoncoders_photo':
                field.upload_to = 'photos/%d' % self.id
        super(PythonCoders, self).save()    

    def __unicode__(self):
        return self.author_name.username
        
    class Meta:
        verbose_name_plural = "Python Severler"
    
    
#    class SpecialImageField(ImageField):
#        
#        def get_directory_name(self):
#            if callable(self.upload_to):
#                return self.upload_to()
#            else:
#                return super(SpecialImageField, self).get_directory_name()
