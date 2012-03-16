# -*- coding: utf-8 -*-

from django.db import models


class Link(models.Model):
    """
        Bağlantıları depolamak için kullanılacak
        model.
        
        title, href, description alanlarını içerir.
    """
    
    title = models.CharField('Başlık', max_length = 255)
    href = models.URLField('Adres', max_length = 255)
    description = models.TextField('Kısa açıklama', max_length = 570, blank = True, null = True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title
    
    def anchor_tag(self):
        return "<a href='%s' target='_blank'>%s</a>" % (self.href, self.title)
    
    class Meta:
        verbose_name = 'Bağlantı'
        verbose_name_plural = 'Bağlantılar'
        
        ordering = ['-created_at']