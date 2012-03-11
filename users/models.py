# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.contrib.localflavor.tr.tr_provinces import PROVINCE_CHOICES

class Profile(models.Model):
    """
        Üye bilgilerini depolamak için kullanılacak olan
        profil modeli.
        
        web_site, about, city, user
    """
        
    web_site = models.URLField('Web Adresi', max_length = 255, blank = True, null = True)
    about = models.TextField(verbose_name = 'Hakkımda', max_length = 500, blank = True, null = True)
    city = models.CharField(
                               choices = PROVINCE_CHOICES,
                               verbose_name = 'Şehir', blank = True, null = True,
                               max_length = 2
                               )
    
    user = models.OneToOneField(User, verbose_name = 'Üye')
    
    def __unicode__(self):
        return self.user.username
        
    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profiller'
    
    
