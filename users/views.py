# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import logout

from pythontr_org.users.forms import UserSettings, ProfileForm
from pythontr_org.users.models import Profile


def signup(request):
    """
        Kayıt olma işlemi için kullanılır.
    """
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user = user)
            
            return redirect('posts:index')
    else:
        form = UserCreationForm()
        
    return render(request, 'users/signup.html', locals())


@login_required
def settings(request):
    """
        Kullanıcı ayarlarına ulaşmak için bir panel.
        Şifre değiştirme, hesabı silme, profili düzenleme,
        kişisel bilgileri düzenleme formlarına ulaşılır.
    """
    
    
    return render(request, 'users/settings.html')

@login_required
def update_informations(request):
    """
        Kişisel bilgileri güncelleme formu.
        first_name, email, last_name
    """
    
    if request.method == 'POST':
        form = UserSettings(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Kişisel bilgileriniz başarı ile kaydedildi.')
            
            return redirect('users:settings')
    else:
        form = UserSettings(instance = request.user)
        
    return render(request, 'users/update_informations.html', locals())


@login_required
def update_profile(request):
    """
        Profil bilgilerini güncelleme formu.
        web_site, about, city
    """
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = request.user.get_profile())

        if form.is_valid():
            form.save()
            messages.success(request, 'Profil bilgileriniz başarı ile kaydedildi.')
            
            return redirect('users:settings')
    else:
        form = ProfileForm(instance = request.user.get_profile())
        
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


def show(request, username):
    """
        Üyenin herkes tarafından görülebilen profili.
        Temel bilgileri ve eğer yazarsa yazar bilgileri gösterilir.
    """
    
    tuser = get_object_or_404(User, username = username)
    profile = tuser.get_profile()
    
    is_me = tuser.username == request.user.username

    group = Group.objects.get(name = 'Yazarlar')    
    if group.user_set.filter(username = tuser): # üye yazarsa
        
        is_author = True
        posts = tuser.post_set.filter(published = True)
    
    return render(request, 'users/show.html', locals())


def authors(request):
    """
        django.contrib.auth.models.Group adlı modelde 'Yazarlar'
        olarak kayıtlı üyeleri listele.
        
        Bu kişiler yeni gönderi ekleme yetkisine sahip.
    """
    
    group = get_object_or_404(Group, name = 'Yazarlar')
    users = group.user_set.all()
    
    return render(request, 'users/authors.html', locals())
    
    