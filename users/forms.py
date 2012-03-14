# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User

from pythontr_org.users.models import Profile


class UserSettings(ModelForm):
    class Meta:
        model = User
        
        fields = ('email', 'first_name', 'last_name')
        
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        
        exclude = ('user', )
        
        widgets = {
                   'city': forms.Select(attrs = {'class': 'input-xlarge'}),
        }
        