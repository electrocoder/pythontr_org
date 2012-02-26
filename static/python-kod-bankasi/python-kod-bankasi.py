# -*- coding: utf-8-*-
# Projenin Adi : Python Kod Bankası
# Tarih : 2008-2011
# Yazar : pythontr.org ekibi
# Kontak : admin@pythontr.org
# Web : http://www.pythontr.org
# Python Versiyonu : 2.6-2.7
# Amaci : www.pythontr.org sitesi üzerinde kod bankası oluşturulması.
#         Eklemek isteginiz kodlar icin irtibat kurunuz...
#
#         http://www.pythontr.org
#
#Python kod bankasi isimli programa kod listesini hazirlar.
import re
import urllib
import os

#url = "http://www.pythontr.org/python-kod-bankasi-liste/python-kod-bankasi-liste.html"

#f = urllib.urlopen(url)
#hfile=open("python-kod-bankasi-liste.html",'w')
hfile1=open("python-kod-bankasi-liste.html",'w')
dosyalistesi=os.listdir(os.getcwd())

##for i in f:
##    print i
##    hfile.write(i+"<br>")
##    hfile.write('\n')

for i in dosyalistesi:
    print i
    hfile1.write(i+"<br>")
    hfile1.write('\n')

#hfile.close()
hfile1.close()
