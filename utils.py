# -*- coding: utf-8 -*-

import unicodedata, re
from django.utils.safestring import mark_safe

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import View

def slugify_unicode(value):
    """
        Türkçe karakterleri yutmayan slugify fonksiyonu.
        http://gokmengorgen.net/post/detail/djangoda-turkce-destekli-slugify/
    """
    
    value = value.replace(u'\u0131', 'i')
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    
    return mark_safe(re.sub('[-\s]+', '-', value))


class ProtectedView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)