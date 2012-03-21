# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


from pythontr_org.links.models import Link



class LinksFunctionalTests(TestCase):
    
    fixtures = ['links.json']
    
    
    def test_index_page(self):
        """
            Bağlantılar anasayfasını test eder.
        """

        response = self.client.get(reverse('links:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['links'])
        
        self.assertEqual(len(Link.objects.all()), len(response.context['links']))
        