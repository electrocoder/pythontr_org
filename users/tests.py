# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User, Group

from django.core.urlresolvers import reverse

class FunctionalTests(TestCase):
    
    fixtures = ['auth.json', 'users.json']
    
    
    def setUp(self):
        
        self.user_informations = {
                                  'username': 'frodo',
                                  'password1': 'thering',
                                  'password2': 'thering'
        }
        
        self.client.login(username='frodo', password='thering')
    
    
    def test_get_signup_page(self):
        """
            Kayıt olma testi yapar.
        """
        
        
        response = self.client.get(reverse('users:signup'))
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])
        
        
    def test_post_signup_page(self):
        """
            Kayıt olma sayfasındaki formu doldurup gönderir.
        """
        
        response = self.client.post(reverse('users:signup'), self.user_informations)
        
        self.assertRedirects(response, reverse('users:settings'))        
        self.assertTrue(User.objects.get(username = self.user_informations['username']))
        
        
    def test_get_settings_page(self):
        """
            Kullanıcı ayarları sayfasına gitme testi.
        """
        
        response = self.client.get(reverse('users:settings'))
        
        self.assertEqual(response.status_code, 200)
        
        
    def test_get_update_informations_page(self):
        """
            Kişisel bilgilerini güncelleme sayfasına gitme testi.
        """
        
        response = self.client.get(reverse('users:update_informations'))
        print response.content
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])
        
        
    def test_post_update_informations_page(self):
        """
            Kişisel bilgileri güncelleme sayfasına istek yapma testi.
        """
        
        settings = {
                    'email': 'frodo@gmail.com',
                    'first_name': 'Frodo',
                    'last_name': 'Baggins'
        }
        
        response = self.client.post(reverse('posts:update_informations'), settings)
        
        user = response.context['user']
        
        print user
        
        
        