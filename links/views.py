# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from pythontr_org.links.models import Link
from pythontr_org.links.forms import LinkForm

from pythontr_org.links.mails import LinkAddedMail
from pythontr_org.utils import links_object_list


def index(request):
    """
        Bağlantıları listeler.
    """    
    return links_object_list(
                             request,
                             Link.objects.filter(confirmed=True),
                             template_name='index.html'
                             )


@login_required
def new(request):
    """
        Yeni bağlantı eklemek için kullanılır.
        Bağlantı kaydedilir, yöneticilere mail gönderilir.
    """
    
    form = LinkForm(request.POST or None, instance = Link(confirmed = False))
    
    if form.is_valid():
        link = form.save()
        
        LinkAddedMail(link).send()
        
        messages.success(request, u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.')        
        return redirect('users:settings')
    
    return render(request, 'links/new.html', locals())