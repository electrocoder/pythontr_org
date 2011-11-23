# -*- coding: utf-8-*-
# Projenin Adi : PythonTR-Türk Python' cular...
# Tarih : 2008-2011
# Yazar : pythontr.org ekibi
# Kontak : admin@pythontr.org
# Web : http://pythontr.org
# Python Versiyonu : 2.6-2.7
# Django Versiyonu : 1.2.5
# Amaci : www.pythontr.org sitesinin Django framework ile acik kaynakli kodlanmasi...
#         Eklemek isteginiz kodlar icin irtibat kurunuz...
#
#         http://pythontr.org
#
from django.db import models
import datetime

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return self.question
	
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
	class Meta:
		verbose_name_plural = "Anketler"    #admin sayfamizda hangi isimle gorunsun
		verbose_name = "Anket"
		
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	
	def __unicode__(self):
		return self.choice
	