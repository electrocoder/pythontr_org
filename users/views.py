# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from django.contrib.auth import logout

from pythontr_org.users.forms import UserSettings, ProfileForm
from pythontr_org.users.models import Profile

from pythontr_org.utils import AuthorListView, UserPostListView, SettingsView

# class-based generic views

profile = UserPostListView.as_view()
authors = AuthorListView.as_view()
settings = SettingsView.as_view()


def signup(request):
    """
        Kayıt olma işlemi için kullanılır.
    """
    
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        
        login(request, user)
        
        Profile.objects.create(user = user)
        
        messages.success(request, u'Sisteme hoşgeldiniz. Sizi aramızda görmek bize büyük bir mutluluk verdi.')
        
        return redirect('users:settings')
        
    return render(request, 'users/signup.html', locals())


@login_required
def update_informations(request):
    """
        Kişisel bilgileri güncelleme formu.
        first_name, email, last_name
    """
    
    form = UserSettings(request.POST or None, instance = request.user)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, 'Kişisel bilgileriniz başarı ile kaydedildi.')
        
        return redirect('users:settings')

        
    return render(request, 'users/update_informations.html', locals())


@login_required
def update_profile(request):
    """
        Profil bilgilerini güncelleme formu.
        web_site, about, city
    """
    
    form = ProfileForm(request.POST or None, instance = request.user.get_profile())

    if form.is_valid():
        form.save()
        messages.success(request, 'Profil bilgileriniz başarı ile kaydedildi.')
        
        return redirect('users:settings')
            
    return render(request, 'users/update_profile.html', locals())
    

@login_required
def disable(request):
    """
        Üyenin is_active özelliğini pasif yapar.
        Veritabanından silinmez fakat üye giriş yapamaz.
    """
    
    user = User.objects.get(username = request.user)    
    user.is_active = False
    
    user.save()
    logout(request)
    
    return redirect('posts:index')