# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib.auth import authenticate, login
from django.forms.formsets import formset_factory

from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from django.contrib.auth import logout

from pythontr_org.users.forms import UserSettings, ProfileForm, InviteFriendForm
from pythontr_org.users.models import Profile
from pythontr_org.users.mails import invite_friend_mail


class SettingsView(TemplateView):
    template_name='users/settings.html'
    
    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)        
        group   = Group.objects.get(name='Yazar olmak isteyenler')
        
        if group.user_set.filter(username=self.request.user):
            context['author_request_send'] = True
        
        return context    

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SettingsView, self).dispatch(*args, **kwargs)


class AuthorListView(ListView):
    template_name='users/authors.html'
    paginate_by=30
    
    template_object_name='user'
    
    group=Group.objects.get(name='Yazarlar')
    queryset=group.user_set.filter(is_active=True)


class PeopleListView(AuthorListView):
    template_name='users/people.html'    
    queryset=Group.objects.get(name='Sıradan üyeler').user_set.filter(is_active=True)
    

class UserPostListView(ListView):
    paginate_by=6
    template_name='users/profile.html'
    
    template_object_name='post'
    
    
    def get_queryset(self):
        self.tuser = get_object_or_404(User, username=self.kwargs['username'])
        self.profile = self.tuser.get_profile()
        
        self.group = Group.objects.get(name='Yazarlar')
        
        if self.group.user_set.filter(username=self.tuser):
            return self.tuser.post_set.filter(published=True)
        else:
            return []
        
    
    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        
        context.update({
                            'group': self.group,
                            'profile': self.profile,
                            'tuser': self.tuser,
                        }) 
        
        return context


def signup(request):
    """
        Kayıt olma işlemi için kullanılır.
    """
    
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.groups.add(Group.objects.get(name='Sıradan üyeler'))
        
        login(request, user)        
        Profile.objects.create(user = user)        
        
        messages.success(request, u'Sisteme hoşgeldiniz. Sizi aramızda görmek bize büyük bir mutluluk verdi.')
        
        return redirect('users:settings')
        
    return render(request, 'users/signup.html', locals())


@login_required
def invite_friends(request):
    """
        Üyelerin arkadaşlarını davet etmesini sağlayan fonksiyon.
    """
    FriendsFormset = formset_factory(InviteFriendForm, extra=request.GET.get('extra', 3))
    
    
    if request.method == 'POST':
        friend_formset = FriendsFormset(request.POST, request.FILES)
        
        if friend_formset.is_valid():
            invite_friend_mail(request.user, friend_formset.cleaned_data)
    else:
        friend_formset = FriendsFormset()                
    
    return render(request, 'users/invite_friends.html', locals())


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