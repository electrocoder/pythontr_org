# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from pythontr_org.main.forms import ContactForm
from pythontr_org.main.mails import ContactMail, AuthorMail


def contact(request): 
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        
        ContactMail(form).send()
        return redirect('posts:index')                    
    
    return render(request, 'main/contact.html', locals())


@login_required
def became_an_author(request):    
    group         = Group.objects.get(name='Yazar olmak isteyenler')
    authors_group = Group.objects.get(name='Yazarlar')
    
    
    if group.user_set.filter(username=request.user):
        messages.success(request, u'Hali hazırda bir isteğiniz bulunmaktadır. Lütfen isteğinizin işlenmesini bekleyin.')
        
        return redirect('users:settings')
    
    
    if authors_group.user_set.filter(username=request.user):
        return redirect('users:settings')
    
    
    if request.method == 'POST':
        # Üyeyi 'Yazar olmak isteyenler' adlı gruba ekle
        
        group.user_set.add(request.user)        
        AuthorMail(request.user).send()
        
        messages.success(request, u'İsteğiniz gönderilmiştir. Onaylandığında gönderi ekleyebileceksiniz.')        
        return redirect('users:settings')
        
    return render(request, 'main/became_an_author.html', locals())