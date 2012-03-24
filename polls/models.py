# -*- coding: utf-8-*-

from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError


class Poll(models.Model):
	question = models.CharField(max_length=200, verbose_name = "Sorusu")	
	slug = models.SlugField(verbose_name = 'Link', max_length=200)
	
	pub_date = models.DateTimeField("Yayınlanma tarihi", auto_now_add = True)
	
	
	def __unicode__(self):
		return self.question
	
	
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
	
	@models.permalink
	def get_absolute_url(self):
		return ('polls:detail', [self.slug])
	
	
	class Meta:
		verbose_name_plural = "Anketler"
		verbose_name = "Anket"
		
		ordering = ['-pub_date']


class Choice(models.Model):
	poll = models.ForeignKey(Poll, verbose_name = "Anket")
	choice = models.CharField(max_length=200, verbose_name = "Seçenek")
	votes = models.IntegerField(verbose_name = "Oylar", default=0)
	
	
	def __unicode__(self):
		return self.choice
	
	
	class Meta:
		verbose_name = 'Seçenek'
		verbose_name_plural = 'Seçenekler'
		
		
class Vote(models.Model):
	user = models.ForeignKey(User, verbose_name = 'Kullanıcı')
	poll = models.ForeignKey(Poll, verbose_name = 'Anket')
	choice = models.ForeignKey(Choice, verbose_name = 'Seçenek')
	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return self.poll.question
	
	
	def save(self, force_insert=False, force_update=False):
		
		if Vote.objects.filter(user=self.user, poll=self.poll):
			raise ValidationError(u'Bu ankete oy kullanmışsınız.')
	
		super(Vote, self).save(force_insert, force_update)
		
		
	def delete(self):
		self.choice.votes -= 1
		self.choice.save()
		
		super(Vote, self).delete()
	
	
	class Meta:
		ordering = ['-created_at']
		
		verbose_name = 'Oy'
		verbose_name_plural = 'Oylar'