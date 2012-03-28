# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from django.core import mail
from pythontr_org.links.models import Link

from pythontr_org.settings import ADMINS


DATA = {
        'title': 'lorem ipsum dolar sit amet!',
        'href': 'http://127.0.0.1'
}

CONFIRMED_TEXT = u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.'


class LinkAnonymousFunctionalTests(TestCase):
    fixtures     = ['links.json']
    expected_url = "%s?next=%s" % (reverse('users:login'), reverse('links:new'))
    
    
    def test_get_index(self):
        response = self.client.get(reverse('links:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['link_list'])
        
        for link in response.context['link_list']:
            self.assertTrue(link.confirmed)
            
        self.assertEqual(Link.objects.confirmed().count(), len(response.context['link_list']))
        
        # Bağlantılarda sadece bir tane onaylanmamış var.
        # Böylece links:index'de onaylanmayan bağlantıların
        # listelenmediğinden emin oluyoruz.
        
        self.assertFalse(Link.objects.get(confirmed=False) in response.context['link_list'])
        
            
    def test_get_new(self):
        response = self.client.get(reverse('links:new'), follow=True)
        
        self.assertRedirects(response, self.expected_url)
    
    
    def test_post_new(self):
        response = self.client.post(reverse('links:new'), DATA, follow=True)
        
        self.assertRedirects(response, self.expected_url)
        
        
class LinkAuthenticatedUserFunctionalTests(TestCase):
    fixtures = ['links.json', 'groups.json', 'users.json']
    
    
    def setUp(self):
        self.client.login(username='yigit', password='1234')
        
    
    # index için yapılacak test LinkAnonymousFunctionalTests.test_get_index
    # metodu ile aynı olacaktır. 
    # Aynı testi tekrar yazmak mantıksız olacağından bu durumda
    # 'test_get_index' yazılmamıştır.
    
        
    def test_get_new(self):
        response = self.client.get(reverse('links:new'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'])
        
    
    def test_post_new(self):
        count    = Link.objects.count()        
        response = self.client.post(reverse('links:new'), DATA, follow=True)

        
        self.assertRedirects(response, reverse('users:settings'))
        self.assertContains(response, CONFIRMED_TEXT)
        
        self.assertNotEqual(count, Link.objects.count())
        self.assertEqual(Link.objects.latest().title, DATA['title'])
        
        self.assertFalse(Link.objects.latest().confirmed)
        self.assertEqual(len(mail.outbox), 1)
        
        self.assertEqual([email for admin, email in ADMINS], mail.outbox[0].to)
        self.assertEqual(u'Yeni bağlantı eklendi.', mail.outbox[0].subject)


class LinkUnitTests(TestCase):
    fixtures = ['links.json']
    

    def test_anchor_tag(self):
        """
            'anchor_tag' fonksiyonunu test eder.
        """
        
        link = Link.objects.get(pk=1)        
        str  = "<a href='%s' target='_blank'>%s</a>" % (link.href, link.title)
        
        self.assertEqual(link.anchor_tag(), str)