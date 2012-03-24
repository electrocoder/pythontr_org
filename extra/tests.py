# -*- coding: utf-8 -*-

from django.test import TestCase


class AboutPageTest(TestCase):
    """
        Hakkımızda sayfası için hazırlanmış test.
    """
    
    def test_should_show_about(self):
        """
        
            Hakkımızda sayfasını göstermelidir.
            
        """
        
        response = self.client.get('about')
        
        self.assertEqual(response.status_code, 200)
        
        
class ExtraTest(TestCase):
    """
        
        İletişim ve erişim engellendi için testler.
    
    """
    
    def test_should_get_contact(self):
        """
            
            İletişim sayfasına erişilebilmeli.
            
        """
        
        response = self.client.get('contact')        
        self.assertEqual(response.status_code, 200)
        
        
    def test_should_post_contact(self):
        """
            
            İletişim sayfasını doldurup gönderibilmeli.
            
        """
        
        form = {
                'title': 'Lorem ipsum dolar sit amet',
                'email': 'yigitsadic@gmail.com',
                'web_site': 'http://127.0.0.1:8000/',
                'content': 'Class aptent taciti sociosqu ad litora torquent per co...' 
        }
        
        response = self.client.post('contact', form)
        
        self.assertRedirects(response, 'posts:index')
