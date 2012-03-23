# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from pythontr_org.links.models import Link
from pythontr_org.links.forms import LinkForm

def index(request):
    """
        Bağlantıları listeler.
    """
    
    links = Link.objects.all()
    
    return render(request, 'links/index.html', locals())


@login_required
def new(request):
    """
        Yeni bağlantı eklemek için kullanılır.
        Bağlantı kaydedilir, yöneticilere mail gönderilir.
    """
    
    form = LinkForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.')
        
        return redirect('users:settings')
    
    return render(request, 'links/new.html', locals())