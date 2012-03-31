# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User, Group

from django.core.urlresolvers import reverse
from django.core import mail

fixtures = ['groups.json', 'users.json', 'profiles.json', 'categories.json', 'posts.json']


class UserFunctionalTestsForAnonymousUser(TestCase):
    fixtures = fixtures
    
    def setUp(self):
        self.author_group = Group.objects.get(name='Yazarlar')
        self.standart_user_group = Group.objects.get(name='Sıradan üyeler')
    
    
    def test_get_author_list(self):
        response = self.client.get(reverse('users:authors'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_list'])
        
        for user in response.context['user_list']:
            self.assertTrue(user in self.author_group.user_set.filter(is_active=True))
            self.assertTrue(user.is_active)
            
    
    def test_get_user_list(self):
        response = self.client.get(reverse('users:people'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user_list'])
        
        for user in response.context['user_list']:
            self.assertTrue(user in self.standart_user_group.user_set.filter(is_active=True))
            self.assertTrue(user.is_active)
            
    
    def test_get_signup(self):
        response = self.client.get(reverse('users:signup'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'])
        
    
    def test_post_signup(self):
        pass
    
    
    def test_get_login(self):
        pass
    
    
    def test_post_login(self):
        pass
    
    
    def test_get_password_change(self):
        pass
    
    
    def test_post_password_change(self):
        pass
    
    
    def test_get_disable(self):
        pass
    
    
    def test_get_settings(self):
        pass
    
    
    def test_get_update_informations(self):
        pass
    
    
    def test_get_update_profile(self):
        pass
    
    
    def test_get_invite_friends(self):
        pass
    
    
    def test_get_show_profile(self):
        pass
            

class UserFunctionalTestsForAuthenticatedUser(TestCase):
    fixtures = fixtures
    
    def setUp(self):
        self.client.login(username='burcu', password='1234')
        self.user = User.objects.get(username='burcu')
        
        
    def test_get_logout(self):
        pass
    
    
    def test_get_settings(self):
        pass
    
    
    def test_get_update_informations(self):
        pass
    
    
    def test_post_update_informations(self):
        pass
    
    
    def test_get_update_profile(self):
        pass
    
    
    def test_post_update_profile(self):
        pass
    
    
    def test_get_invite_friends(self):
        pass
    
    
    def test_post_invite_friends(self):
        pass
    
    
    def test_get_disable(self):
        pass
        
    
class UserFunctionalTestsForAuthors(TestCase):
    fixtures = fixtures
    
    def setUp(self):
        self.client.login(username='yigit', password='1234')        
        self.user = User.objects.get(username='yigit')
        
        
    def test_get_show_profile(self):
        pass
    


class UserUnitTests(TestCase):
    pass