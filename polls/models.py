# -*- coding: utf-8-*-

from django.db import models


class Poll(models.Model):
	question = models.CharField(max_length=200, verbose_name = "Sorusu")
	pub_date = models.DateTimeField("Yayınlanma tarihi", auto_now_add = True)
	
	def __unicode__(self):
		return self.question
	
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
	class Meta:
		verbose_name_plural = "Anketler"
		verbose_name = "Anket"
		
		ordering = ['-pub_date']


class Choice(models.Model):
	poll = models.ForeignKey(Poll, verbose_name = "Anket")
	choice = models.CharField(max_length=200, verbose_name = "Seçenek")
	votes = models.IntegerField(verbose_name = "Oylar", blank = True, null = True)
	
	def __unicode__(self):
		return self.choice
	
	class Meta:
		verbose_name = 'Seçenek'
		verbose_name_plural = 'Seçenekler'