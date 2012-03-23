# -*- coding: utf-8 -*-

from django.db import models
from django.utils.safestring import mark_safe


class Link(models.Model):
    """
    
        Bağlantıları depolamak için kullanılan model.
        
        title, href, description alanlarını içerir.
        
        'anchor_tag' fonksiyonu HTML <a> tagını oluşturur.
        
    """
    
    title = models.CharField('Başlık', max_length = 255)
    href = models.URLField('Adres', max_length = 255)
    description = models.TextField('Kısa açıklama', max_length = 570, blank = True, null = True)
    
    confirmed = models.BooleanField('Onaylandı mı?', default = True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    
    def __unicode__(self):
        return self.title
    
    def anchor_tag(self):
        return mark_safe("<a href='%s' target='_blank'>%s</a>" % (self.href, self.title))
    
    def get_absolute_url(self):
        return self.href
    
    class Meta:
        verbose_name = 'Bağlantı'
        verbose_name_plural = 'Bağlantılar'
        
        ordering = ['-created_at']
        
        get_latest_by = 'created_at'