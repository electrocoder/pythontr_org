# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from django.core import mail
from pythontr_org.links.models import Link

from pythontr_org.settings import ADMINS


class LinksFunctionals(TestCase):    
    fixtures = ['links.json', 'auth.json']
    
    
    def setUp(self):
        self.client.login(username='yigit', password='1234')
        
        self.link_informations = {
                                  'title': 'Django Project',
                                  'href': 'https://www.djangoproject.com/',
        }
        
        self.CONFIRMED_TEXT = u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.'
    
    
    def test_index_page(self):
        """
            Bağlantılar anasayfasını test eder.
        """

        response = self.client.get(reverse('links:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['link_list'])
        
        self.assertEqual(Link.objects.confirmed().count(), len(response.context['link_list']))
    
    
    def test_get_new_link_page(self):
        """
            Yeni bağlantı ekleme sayfasına GET isteği yap.
        """
        
        response = self.client.get(reverse('links:new'))
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])
      
        
    def test_post_new_link_page(self):
        """
            Yeni bağlantı ekleme sayfasına POST isteği yapar.
        """
        
        count = Link.objects.count()
        
        response = self.client.post(reverse('links:new'), self.link_informations, follow=True)
        
        self.assertRedirects(response, reverse('users:settings'))
        self.assertContains(response, self.CONFIRMED_TEXT)
        
        self.assertNotEqual(count, Link.objects.count())
        self.assertEqual(Link.objects.latest().title, self.link_informations['title'])
        
        self.assertFalse(Link.objects.latest().confirmed)
        self.assertEqual(len(mail.outbox), 1)
        
        self.assertEqual([email for admin, email in ADMINS], mail.outbox[0].to)
        self.assertEqual(u'Yeni bağlantı eklendi.', mail.outbox[0].subject)
        
        
    def test_should_redirect_to_login_page(self):
        """
            Giriş yapmadan bağlantı ekleme sayfasına erişmeyi
            test et.
        """
        
        self.client.logout()
        response = self.client.get(reverse('links:new'))
        
        self.assertRedirects(response, '%s?next=%s' % (reverse('users:login'), reverse('links:new')))
        

class LinkUnits(TestCase):
    """
        Bağlantı modelinin unit testleri.
    """
    
    fixtures = ['auth.json', 'links.json']
    
    
    def setUp(self):
        self.link_informations = {
                                  'title': 'Django Project',
                                  'href': 'https://www.djangoproject.com/',
        }
    
    
    def test_create_new_link(self):
        """
            Yeni bağlantı yaratma test.
        """
        
        link = Link.objects.create(**self.link_informations)
        
        self.assertTrue(link)
        
    def test_anchor_tag(self):
        """
            'anchor_tag' fonksiyonunu test eder.
        """
        
        link = Link.objects.get(pk=2)
        
        str = "<a href='%s' target='_blank'>%s</a>" % ('https://www.djangoproject.com/', 'Django Project')
        
        self.assertEqual(link.anchor_tag(), str)
        
        