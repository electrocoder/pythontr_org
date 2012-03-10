# -*- coding: utf-8-*-

from django.db import models
import datetime

class Poll(models.Model):
	question = models.CharField(max_length=200, verbose_name = "Sorusu")
	pub_date = models.DateTimeField("Yayınlanma tarihi")
	
	def __unicode__(self):
		return self.question
	
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
	class Meta:
		verbose_name_plural = "Anketler"
		verbose_name = "Anket"



class Choice(models.Model):
	poll = models.ForeignKey(Poll, verbose_name = "Anket")
	choice = models.CharField(max_length=200, verbose_name = "Seçenek")
	votes = models.IntegerField(verbose_name = "Oylar")
	
	def __unicode__(self):
		return self.choice