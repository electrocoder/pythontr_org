# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from pythontr_org.users.models import Profile


class UserSettings(ModelForm):    
    def __init__(self, *args, **kwargs):
        super(UserSettings, self).__init__(*args, **kwargs)
        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'
    
        
    class Meta:
        model = User
        
        fields = ('email', 'first_name', 'last_name')
        
        
class ProfileForm(ModelForm):    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'
    
    
    class Meta:
        model = Profile
        
        exclude = ('user', )


class InviteFriendForm(forms.Form):
    name = forms.CharField(max_length=75, label=u'İsim')
    email = forms.EmailField(label='E-posta')