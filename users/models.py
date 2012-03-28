# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
from django.contrib.localflavor.tr.tr_provinces import PROVINCE_CHOICES

from hashlib import md5


TEXTILE_LINK = '''
    <a href='http://en.wikipedia.org/wiki/Textile_%28markup_language%29' target='_blank'>
        Textile
    </a>
'''


class Profile(models.Model):
    """
        Üye bilgilerini depolamak için kullanılacak olan
        profil modeli.
        
        web_site, about, city, user
    """
    user = models.OneToOneField(User, verbose_name='Üye')
        
    web_site = models.URLField('Web Adresi', max_length=255, blank=True, null=True)
    about = models.TextField('Hakkımda', max_length=500, blank= True, null=True,
                             help_text=mark_safe('Bu alanda %s işaretleme dili kullanabilirsiniz.' % TEXTILE_LINK))
    city = models.CharField(
                               choices=PROVINCE_CHOICES,
                               verbose_name='Şehir', blank=True, null=True,
                               max_length=2
                               )
    
    # links
    
    django_people_profile   = models.URLField('Django People profili', blank=True, null=True)
    django_snippets_profile = models.URLField('Django Snippets profili', blank=True, null=True)    
    tuxhub_profile          = models.URLField('Tuxhub profili', blank=True, null=True)
    twitter_profile         = models.URLField('Twitter profili', blank=True, null=True)    
    github_profile          = models.URLField('Github profili', blank=True, null=True)    
    
    
    def __unicode__(self):
        return self.user.username

    def get_image(self, size=200):
        """
            Gravatardan kullanıcını mailine kayıtlı
            profil resmini getir.
        """
        
        url = 'http://www.gravatar.com/avatar/'
        
        
        m = md5()
        m.update(self.user.email)
        
        return url + m.hexdigest() + '?s=%s' % size
                
    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profiller'
        
        ordering = ['user']