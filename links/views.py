# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from pythontr_org.links.models import Link
from pythontr_org.links.forms import LinkForm
from pythontr_org.links.mails import LinkAddedMail


class LinkListView(ListView):
    template_name        = 'links/index.html'
    template_object_name = 'link_list'
    paginate_by          = 15
    queryset             = Link.objects.confirmed()
    


@login_required
def new(request):
    """
        Yeni bağlantı eklemek için kullanılır.
        Bağlantı kaydedilir, yöneticilere mail gönderilir.
    """
    
    form = LinkForm(request.POST or None, instance = Link(confirmed = False))
    
    if form.is_valid():
        link = form.save()
        
        LinkAddedMail(link)
        
        messages.success(request, u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.')        
        return redirect('users:settings')
    
    return render(request, 'links/new.html', locals())