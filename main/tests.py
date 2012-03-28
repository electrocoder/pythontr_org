# -*- coding: utf-8 -*-

from django.test import TestCase

from django.core import mail
from django.core.urlresolvers import reverse

from pythontr_org.settings import ADMINS
from django.contrib.auth.models import User, Group


class ContactTest(TestCase):
    def test_get_contact(self):
        response = self.client.get(reverse('contact'))
        
        self.assertTrue(response.context['form'])
        self.assertEqual(response.status_code, 200)

        
    def test_post_contact(self):
        data = {
                'title': u'Zeki Müren',
                'content': u'Ah bu şarkıların gözü kor olsun',
                'email': 'email@example.com'
        }
        
        
        response = self.client.post(reverse('contact'), data, follow=True)
        self.assertRedirects(response, reverse('posts:index'))
        
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual([email for admin, email in ADMINS], mail.outbox[0].to)
        self.assertEqual(u'İletişim formu gönderildi.', mail.outbox[0].subject)
        
        
class AuthorActionsForAnonymousUserTest(TestCase):
    fixtures=['groups.json', 'users.json']
    
    
    def setUp(self):
        self.redirect_url = '%s?next=%s' % (reverse('users:login'), reverse('became_an_author'))
    
    
    def test_get_became_an_author(self):
        response = self.client.get(reverse('became_an_author'), follow=True)
        
        self.assertRedirects(response, self.redirect_url)
    
    
    def test_post_became_an_author(self):
        response = self.client.post(reverse('became_an_author'), follow=True)
        
        self.assertRedirects(response, self.redirect_url)
        
        
class AuthorActionsForUser(TestCase):
    fixtures=['groups.json', 'users.json']
    
    
    def setUp(self):
        self.group = Group.objects.get(name='Sıradan üyeler')
        self.client.login(username='niyazi', password='1234')
        self.user = User.objects.get(username='niyazi')
        
        self.user.groups.add(self.group)        
        
        
    def test_get_became_an_author(self):
        response = self.client.get(reverse('became_an_author'))
        
        self.assertEqual(response.status_code, 200)
    
    
    def test_post_became_an_author(self):
        data = {
                'focused_on': "[GUI programlama]"
        }
        response = self.client.post(reverse('became_an_author'), data, follow=True)
        group    = Group.objects.get(name='Yazar olmak isteyenler')
        
        
        self.assertRedirects(response, reverse('users:settings'))
        self.assertContains(response, u'İsteğiniz gönderilmiştir. Onaylandığında gönderi ekleyebileceksiniz. Size e-posta yoluyla geri döneceğiz.')
        
        self.assertTrue(self.user in group.user_set.all())
        self.assertEqual(len(mail.outbox), 1)
        
        self.assertEqual(mail.outbox[0].subject, u'Yazar olmak isteyen var!')
        

class AuthorActionsForAuthor(TestCase):
    fixtures=['groups.json', 'users.json']
    
    
    def setUp(self):
        self.client.login(username='yigit', password='1234')        
        self.user = User.objects.get(username='yigit')
        
                
    def test_get_became_an_author(self):
        response = self.client.get(reverse('became_an_author'), follow=True)
        
        self.assertRedirects(response, reverse('users:settings'))
        
        
    def test_post_became_an_author(self):
        response = self.client.post(reverse('became_an_author'), follow=True)
        
        self.assertRedirects(response, reverse('users:settings'))
        