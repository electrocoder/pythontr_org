# -*- coding: utf -8-*-

from django.test import TestCase
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from pythontr_org.polls.models import Poll, Vote, Choice


fixtures = ['groups.json', 'users.json', 'polls.json']


class PollFunctionalTestsForAnonymousUser(TestCase):
    fixtures = fixtures
    poll     = Poll.objects.get(pk=1)

    
    def test_get_index(self):
        response = self.client.get(reverse('polls:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['poll_list'])
        
        self.assertEqual(Poll.objects.count(), len(response.context['poll_list']))
        
        
    def test_get_detail(self):
        response = self.client.get(reverse('polls:detail', args=[self.poll.slug]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['poll'])
        
        self.assertEqual(response.context['poll'].question, self.poll.question)
        
        
    def test_get_results(self):
        response = self.client.get(reverse('polls:results', args=[self.poll.slug]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['poll'])
        
        self.assertEqual(response.context['poll'].question, self.poll.question)
        
        
    def test_post_vote(self):
        response     = self.client.post(reverse('polls:vote', args=[self.poll.slug]), follow=True)
        redirect_url = '%s?next=%s' % (reverse('users:login'), reverse('polls:vote', args=[self.poll.slug]))
        
        self.assertRedirects(response, redirect_url)        
        

class PollFunctionalTestsForAuthenticatedUser(TestCase):
    fixtures = fixtures
    
    
    def setUp(self):
        self.client.login(username='yigit', password='1234')
        self.user = User.objects.get(username='yigit')
        
        self.poll1 = Poll.objects.get(pk=1)
        self.poll2 = Poll.objects.get(pk=2)
            
    # yigit adlı üye 2. ankete oy kullanmıştır.
    # Fakat 1. ankete oy kullanmamıştır.
    # Şimdi gereken detail'e gittiğinde uyarı mesajı almak.
    
    def test_get_detail_for_voted_user(self):
        response = self.client.get(reverse('polls:detail', args=[self.poll2.slug]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['vote'])
        self.assertTrue(response.context['poll'])
        
        self.assertContains(response, u'Bu ankete oy kullanmışsınız.')        
        self.assertEqual(response.context['vote'].poll.question, self.poll2.question)
        
        
    def test_get_detail_for_unvoted_user(self):
        response = self.client.get(reverse('polls:detail', args=[self.poll1.slug]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['poll'])
    
    
    def test_post_vote_for_voted_user(self):
        response = self.client.post(reverse('polls:vote', args=[self.poll2.slug]), {'choice': 5})
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/detail.html')
        
        self.assertTrue(response.context['error_message'])       
        self.assertEqual(response.context['error_message'], u'Bu ankete zaten oy kullanmışsınız.')
        
        
    def test_post_vote_for_voted_user_wrong_param(self):
        response = self.client.post(reverse('polls:vote', args=[self.poll2.slug]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/detail.html')

        
        self.assertTrue(response.context['error_message'])
        self.assertEqual(response.context['error_message'], u'Bir seçeneği seçmediniz.')
            
    
    def test_post_vote_for_unvoted_user(self):
        old_vote_count = self.poll1.choice_set.get(pk=1).votes
        response       = self.client.post(reverse('polls:vote', args=[self.poll1.slug]), {'choice': 1}, follow=True)
        new_vote_count = Poll.objects.get(pk=1).choice_set.get(pk=1).votes
        
        
        self.assertRedirects(response, reverse('polls:results', args=[self.poll1.slug]))
        self.assertNotEqual(old_vote_count, new_vote_count)
        
        vote = Vote.objects.filter(user=self.user, poll=self.poll1)
        
        self.assertTrue(vote)
        self.assertEqual(vote[0].poll, self.poll1)
        self.assertEqual(vote[0].choice.id, 1)
        
    
    def test_get_vote_back_for_voted(self):
        response = self.client.get(reverse('polls:vote_back', args=[self.poll2.slug]), follow=True)
        
        
        

    
class VoteUnitTests(TestCase):
    pass