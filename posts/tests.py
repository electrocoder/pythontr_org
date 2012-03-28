# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from pythontr_org.posts.models import Post, Category
from django.contrib.auth.models import User


NEW_DATA = {
            'title': 'Lorem',
            'category': 1,
            'content': 'Text',
            'published': True,
}

fixtures = ['categories.json', 'groups.json', 'users.json', 'posts.json']


class PostAnonymousFunctionalTests(TestCase):
    fixtures = fixtures
    
    def setUp(self):
        self.post                = Post.objects.published()[0]
                
        self.new_redirect_url    = '%s?next=%s' % (reverse('users:login'), reverse('posts:new'))
        self.edit_redirect_url   = '%s?next=%s' % (reverse('users:login'), reverse('posts:edit', args=[self.post.id]))
        self.delete_redirect_url = '%s?next=%s' % (reverse('users:login'), reverse('posts:delete', args=[self.post.id]))
    
    
    def test_get_index(self):
        response = self.client.get(reverse('posts:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['post_list'])        
        self.assertEqual(Post.objects.published().count(), len(response.context['post_list']))
        
        for post in response.context['post_list']:
            self.assertTrue(post.published)
        
    
    def test_get_show(self):
        posts = Post.objects.published()
        
        for post in posts:
            old_count = post.read_count
            response  = self.client.get(reverse('posts:show', args=[post.category.slug, post.slug]))
            
            self.assertEqual(response.status_code, 200)
            
            # Her şey alan aynı mı test et.
            
            self.assertEqual(post.title, response.context['post'].title)
            self.assertEqual(post.slug, response.context['post'].slug)
            self.assertEqual(post.content, response.context['post'].content)            
            self.assertEqual(post.author, response.context['post'].author)
            self.assertEqual(post.tags, response.context['post'].tags)
                    
            self.assertTrue(response.context['post'].published)
            
            # Okunma sayısı artmış mı? - İki yoldan test et.
            new_count = response.context['post'].read_count
            
            self.assertNotEqual(old_count, new_count)
            self.assertEqual(old_count + 1, new_count)
    
    
    def test_get_show_unpublished(self):
        posts = Post.objects.filter(published=False)
        
        for post in posts:
            response = self.client.get(reverse('posts:show', args=[post.category.slug, post.slug]))
            
            self.assertEqual(response.status_code, 404)
            self.assertFalse(post.published)
            
            
    def test_get_search(self):
        q        = 'Nullam'
        response = self.client.get(reverse('posts:search'), {'q': q})
        
        self.assertTrue(response.context['post_list'])
        self.assertEqual(response.status_code, 200)
        
        for post in response.context['post_list']:
            self.assertTrue(post.published)
            self.assertTrue(q in post.content)
        
            
    def test_get_my_posts(self):
        response = self.client.get(reverse('posts:my_posts'), follow=True)
        
        self.assertRedirects(response, '%s?next=%s' % (reverse('users:login'), reverse('posts:my_posts')))
        
    
    def test_get_new(self):
        response = self.client.get(reverse('posts:new'), follow=True)
        
        self.assertRedirects(response, self.new_redirect_url)
    
    
    def test_post_new(self):
        response = self.client.post(reverse('posts:new'), NEW_DATA, follow=True)
        
        self.assertRedirects(response, self.new_redirect_url)


    def test_get_edit(self):        
        response = self.client.get(reverse('posts:edit', args=[self.post.id]))
        
        self.assertRedirects(response, self.edit_redirect_url)
        
        
    def test_post_edit(self):
        response = self.client.post(reverse('posts:edit', args=[self.post.id]))
        
        self.assertRedirects(response, self.edit_redirect_url)
        
    
    def test_get_delete(self):
        response = self.client.get(reverse('posts:delete', args=[self.post.id]))
        
        self.assertRedirects(response, self.delete_redirect_url)
        
        
# 'test_get_search' testlerine kadar olan testler aynı sonuca
# ulaşacağından bu testleri tekrar etmek anlamsız.
# O yüzden bu testler giriş yapmış kullanıcı için
# atlanıcak.        

class PostAuthorFunctionalTests(TestCase):
    fixtures = fixtures
    
    
    def setUp(self):
        self.client.login(username='yigit', password='1234')
        self.user = User.objects.get(username='yigit')
        self.post = self.user.post_set.all()[0]
        
        
        # Gönderi eklemek için ve düzenlemek için
        # gerekli değerler.
        
        self.new_data = {
                         'title': u'Selanik türküsü',
                         'category': 1,
                         'content': u'Mezarımı kazın bre dostlar',
                         'published': True
        }
        
        self.edit_data = {
                          'title': u'Kızılcıklar oldu mu?',
                          'category': 2,
                          'content': u'Selelere doldu mu?',
                          'published': True,
        }
        
        
    def test_get_my_posts(self):
        posts_count = self.user.post_set.count()
        response    = self.client.get(reverse('posts:my_posts'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['post_list'])        
        self.assertEqual(len(response.context['post_list']), posts_count)
        
        for post in response.context['post_list']:
            self.assertTrue(post.author == self.user)
            

    def test_get_new(self):
        response = self.client.get(reverse('posts:new'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'])
        
    
    def test_post_new(self):
        old_post_count = self.user.post_set.count()
        response       = self.client.post(reverse('posts:new'), self.new_data, follow=True)
        post           = self.user.post_set.latest()
        new_post_count = self.user.post_set.count()
        
        
        self.assertRedirects(response, reverse('posts:my_posts'))
        self.assertNotEqual(old_post_count, new_post_count)
        
        self.assertEqual(old_post_count + 1, new_post_count)
        self.assertContains(response, u'Gönderi başarı ile eklendi.')
        
        self.assertEqual(post.title, self.new_data['title'])
        self.assertEqual(post.content, self.new_data['content'])
        
        self.assertEqual(post.category.id, self.new_data['category'])
        self.assertEqual(post.published, self.new_data['published'])
        
        
    def test_get_edit(self):
        response = self.client.get(reverse('posts:edit', args=[self.post.id]))
        form     = response.context['form']
        
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'])
        
        self.assertEqual(form['title'].value(), self.post.title)
        self.assertEqual(form['category'].value(), self.post.category.id)
        
        self.assertEqual(form['content'].value(), self.post.content)
        self.assertEqual(form['published'].value(), self.post.published)        
        
        
    def test_post_edit(self):        
        response = self.client.post(reverse('posts:edit', args=[self.post.id]), self.edit_data, follow=True)
        new_post = self.user.post_set.all()[0]
        
        self.assertRedirects(response, reverse('posts:my_posts'))
        self.assertContains(response, u'Gönderi başarı ile düzenlendi.')
        
        self.assertNotEqual(self.post.title, new_post.title)
        self.assertNotEqual(self.post.content, new_post.content)
        self.assertNotEqual(self.post.category, new_post.category)
        self.assertNotEqual(self.post.published, new_post.published)
        
        
    def test_get_delete(self):
        old_post_count = self.user.post_set.count()
        response       = self.client.get(reverse('posts:delete', args=[self.post.id]), follow=True)
        new_post_count = self.user.post_set.count()
        

        self.assertNotEqual(old_post_count, new_post_count)
        self.assertRedirects(response, reverse('posts:my_posts'))
        
        # Dikkat!
        # " karakteri &quot; değerinde HTML'de
        # assertContains'de "" != &quot;&quot;
        
        self.assertContains(response, u'&quot;%s&quot; başlıklı gönderi başarı ile silindi' % self.post.title)
        
        
    def login_orhan(self):
        """
            orhan adlı kullanıcı ile giriş yapılır.
        """
        
        self.client.logout()
        self.client.login(username='orhan', password='1234')
    
    
    # Yazar sadece kendi gönderilerini düzenleyebilir, silebilir.
    # Eğer düzenlenen veya silinen gönderi yazara ait değilse
    # /errors/access_denied/ sayfasına yönlendirilir.
        
    def test_only_posts_author_can_edit(self):
        self.login_orhan()
        
        response = self.client.get(reverse('posts:edit', args=[self.post.id]), follow=True)        
        self.assertRedirects(response, reverse('access_denied'))
        
        
    def test_only_posts_author_can_delete(self):
        self.login_orhan()
        
        response = self.client.get(reverse('posts:delete', args=[self.post.id]), follow=True)
        self.assertRedirects(response, reverse('access_denied'))


# Aynı testi giriş yapmış kullanıcı için yapmaya gerek yok.
# Çünkü bu testlerde giriş ile ilgili bir şey bulunmuyor.

class CategoryAnonymousFunctionalTests(TestCase):
    fixtures = fixtures
    
    def test_get_categories(self):
        response = self.client.get(reverse('posts:categories'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['category_list'])        
        self.assertEqual(Category.objects.count(), len(response.context['category_list']))
    
    
    def test_get_category_show(self):
        category   = Category.objects.get(pk=1)
        posts      = Post.objects.filter(published=True, category=category)
        post_count = category.post_set.filter(published=True).count()
        
        response = self.client.get(reverse('posts:show_category', args=[category.slug]))
        
        self.assertTrue(response.context['post_list'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['post_list']), post_count)
        
        
        for post in response.context['post_list']:
            self.assertTrue(post.category == category)
            self.assertTrue(post.published)
            
    
    def test_get_wrong_category(self):
        category_slug = 'noncategory'
        
        response = self.client.get(reverse('posts:show_category', args=[category_slug]))
        
        self.assertEqual(response.status_code, 404)        