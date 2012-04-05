# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView
from django.views.generic import CreateView

from pythontr_org.links.models import Link
from pythontr_org.links.forms import LinkForm
from pythontr_org.links.mails import LinkAddedMail

from pythontr_org.utils import ProtectedView

class LinkListView(ListView):
    template_name        = 'links/index.html'
    template_object_name = 'link_list'
    paginate_by          = 15
    queryset             = Link.objects.confirmed()


class NewLinkView(CreateView, ProtectedView):
    template_name = 'links/new.html'    
    form_class    = LinkForm
    initial       = {  'href': 'http://'  }
    
    
    def form_valid(self, form):
        link = LinkForm(self.request.POST, instance=Link(confirmed=False))
        link.save()
        
        LinkAddedMail(link)
        
        messages.success(self.request, u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.')
        return redirect('users:settings')
    
    
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(NewLinkView, self).dispatch(*args, **kwargs)