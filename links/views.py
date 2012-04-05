# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import CreateView

from pythontr_org.links.models import Link
from pythontr_org.links.forms import LinkForm
from pythontr_org.links.mails import LinkAddedMail


class LinkListView(ListView):
    template_name        = 'links/index.html'
    template_object_name = 'link_list'
    paginate_by          = 15
    queryset             = Link.objects.confirmed()


class NewLinkView(CreateView):
    success_url = '/'
    template_name = 'links/new.html'
    
    def get_form(self):
        return LinkForm(self.request.POST or None, instance = Link(confirmed=False))
    
    def form_valid(self, form):
        link = LinkForm(self.request.POST)
        link.save()
        
        #LinkAddedMail(link)
        
        messages.success(self.request, u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.')
        


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
        
                
        return redirect('users:settings')
    
    return render(request, 'links/new.html', locals())