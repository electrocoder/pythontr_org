# -*- coding: utf-8 -*-

"""
    'posts' uygulaması için functional ve unit testleri
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

from pythontr_org.posts.models import Post, Category



class PostFunctionals(TestCase):
    """
        'Post' modeli ile ilgili olan fonksiyonları test
        eder.
        'index', 'show', 'search'
    """
    
    fixtures = ['posts.json', 'auth.json']        
    
    def test_get_index(self):
        """
        Index sayfasına istek gönderir.
        200 durum kodu döndürmelidir.
        """
        
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200, 'Gönderiler: posts:index sayfasının testinde durum kodu uyuşmuyor!')
        
        self.assertIsNotNone(response.context['posts'], 'Gönderiler: posts:index sayfasında gönderi yok!')
        
    def test_get_show(self):
        """
        Show sayfasına istek gönderir.
        200 durum kodu döndürmelidir.
        """
        
        posts = Post.objects.filter(published = True)
        
        for post in posts:
            response = self.client.get(reverse('posts:show', args = [post.id, post.slug]))
            
            self.assertEqual(response.status_code, 200, 'Gönderiler: Gönderilerden biri gösterilirken hata oluştu.')
            self.assertEqual(response.context['post'].title, post.title, 'Gönderiler: Gönderilerden biri yok!')
            
            self.assertEqual(post.read_count + 1, response.context['post'].read_count, 'Gönderiler: Gönderinin okunma sayısı artmadı.')
            
            
    def test_get_show_should_return_404(self):
        """
        Show sayfasına istek gönderir.
        Yanlış bir id ile istek yapılır.
        404 hata kodu döndürmelidir.
        """
        
        BAD_IDS = [i for i in range(10, 11)]
        
        for bad in BAD_IDS:
            response = self.client.get(reverse('posts:show', args=[bad, 'wrong!']))
            
            self.assertEqual(response.status_code, 404, 'Gönderiler: 404 Hata kodu döndürmedi!')
            
            
    def test_should_search(self):
        """
        Search sayfasına istek gönderir.
        django ve flask için arama yapar.
        """
        
        SEARCH_DICT = {
                       'django': [Post.objects.get(pk = 1), Post.objects.get(pk=2)],
                       'flask': [Post.objects.get(pk=4)],
        }
        
        # django için ara
        
        response = self.client.get(reverse('posts:search'), {'q': 'django'})
        for p in response.context['posts']:
            self.assertTrue(p in SEARCH_DICT['django'], 'Gönderiler: Django için arama sonuçlarında hata var!')
        
        # flask için ara
        
        response = self.client.get(reverse('posts:search'), {'q': 'flask'})
        self.assertIsNotNone(response.context['posts'], 'Gönderiler: Arama sonucu flask için boş döndü!')
        
        
class CategoryFunctionals(TestCase):
    """
        'Category' modeli ile ilgili functional test.
    """
    
    fixtures = ['posts.json']        
    
    def test_should_get_show_category(self):
        """
            Her kategorideye bağlı gönderileri listeleme
            testi.
        """
        
        categories = Category.objects.filter(pk__in = [1, 3, 4])
        
        for cat in categories:
            response = self.client.get(reverse('posts:show_category', args=[cat.id, cat.slug]))
            
            self.assertEqual(response.status_code, 200, 'Kategoriler: Kategori gösterme başarı ile sonuçlanmadı.')
            self.assertIsNotNone(response.context['posts'], 'Kategoriler: Verilen kategoride gönderi yok!')
        
            self.assertEqual(len(cat.post_set.all()), len(response.context['posts']))
            
            
    def test_should_raise_404_with_bad_id(self):
        """
            Yanlış id verilirse 404 döndürmelidir.
        """
        
        response = self.client.get(reverse('posts:show_category', args=[123, 'hatali']))
        
        self.assertEqual(response.status_code, 404, 'Kategoriler: 404 vermesi gereken yerde bir hata var!')
         