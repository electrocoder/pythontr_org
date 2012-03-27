# -*- coding: utf-8 -*-

import unicodedata, re
from django.utils.safestring import mark_safe


def slugify_unicode(value):
    """
        Türkçe karakterleri yutmayan slugify fonksiyonu.
        http://gokmengorgen.net/post/detail/djangoda-turkce-destekli-slugify/
    """
    
    value = value.replace(u'\u0131', 'i')
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    
    return mark_safe(re.sub('[-\s]+', '-', value))