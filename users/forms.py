# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User

from pythontr_org.users.models import Profile

from django.contrib.localflavor.tr.tr_provinces import PROVINCE_CHOICES

class UserSettings(ModelForm):
    class Meta:
        model = User
        
        fields = ('email', 'first_name', 'last_name')
        
        
class ProfileForm(ModelForm):
    
    city = forms.ChoiceField(PROVINCE_CHOICES,
                             widget = forms.Select(attrs = {'class': 'input-xlarge'})
                             )
    
    class Meta:
        model = Profile
        
        exclude = ('user', )