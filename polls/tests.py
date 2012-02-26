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
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

