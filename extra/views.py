# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from django.contrib import messages

from pythontr_org.extra.forms import ContactForm, AuthorForm

from django.contrib.auth.decorators import login_required

def access_denied(request):
    return render(request, 'extra/access_denied.html')


def contact(request):
    """
        İletişim sayfasını çalıştırır.
        Eğer form gönderilmeye uygun ise
        yöneticilere mail atar.
    """
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()        
    
    return render(request, 'extra/contact.html', locals())


@login_required
def became_an_author(request):
    """
        Yazar olma istek formu.
        'Yazar olmak isteyenler' adlı gruba ekle üyeyi.
        Yöneticiye mail gönder.
    """
    
    group = Group.objects.get(name = 'Yazar olmak isteyenler')
    
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            
            group.user_set.add(request.user) # üyeyi yazar olmak isteyenler adlı
            # gruba ekle
            
            messages.success(request, u'İsteğiniz gönderilmiştir. Onaylandığında gönderi ekleyebileceksiniz.')
            
            return redirect('users:settings')
    else:
        form = AuthorForm()
        
    return render(request, 'extra/became_an_author.html', locals())
    
    