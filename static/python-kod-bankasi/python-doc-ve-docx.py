#! /usr/bin/env python
#-*- coding: utf8 -*-
from docx import * #kütüphane dosyamızı kullanmak için

document = opendocx('iletisim.docx') #2007 formatındaki dosyamızın tam yolu verilmelidir
doc = getdocumenttext(document) #dosyadan okuma yap
for i in doc:
    print i

