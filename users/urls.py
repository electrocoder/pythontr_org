# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout, password_change

from pythontr_org.users.views import SettingsView, AuthorListView,\
UserPostListView, PeopleListView


PASSWORD_CHANGE_DICT = {
                   'template_name': 'users/password_change.html',
                   'post_change_redirect': '/accounts/settings/'
}


urlpatterns = patterns('pythontr_org.users.views',
                       # yazarlar
                       url(r'^authors/$', AuthorListView.as_view(), name='authors'),
                       url(r'^people/$', PeopleListView.as_view(), name='people'),
                       
                       # Giriş ve çıkış
                       url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
                       url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
                       
                       # kayıt olma ve şifre değiştirme
                       url(r'^signup/$', 'signup', name='signup'),
                       url(r'^password_change/$', password_change, PASSWORD_CHANGE_DICT, name='password_change'),
                                           
                       # hesabı dondurma
                       url(r'^disable/$', 'disable', name='disable_account'),
                       
                       # profil gösterme
                       url(r'^profile/(?P<username>\w+)/', UserPostListView.as_view(), name='show_profile'),
                       
                       # profil ve hesap ayarları
                       url(r'^settings/$', SettingsView.as_view(), name='settings'),                       
                       url(r'^settings/update_informations/$', 'update_informations', name='update_informations'),
                       url(r'^settings/update_profile/$', 'update_profile', name='update_profile'),
                       
                       url(r'^invite_friends/$', 'invite_friends', name='invite_friends'),
                       url(r'^password_reset/', include('pythontr_org.users.password_reset_urls')),             
)
