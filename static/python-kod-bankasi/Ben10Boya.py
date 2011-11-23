# Projenin Adi : Ben 10 Boyama Kitabi Yapimi
# Tarih :24-02-2011
# Yazar : Sahin MERSIN
# Iletisim : electrocoder@gmail.com
# Web : http://pythontr.org
# Python Versiyonu : 2.5-2.6

# -*- coding: utf-8 -*-

import ImageFilter
import Image
import os

file=os.listdir(os.getcwd()) # klasordeki tum resim dosyalari

for i in file:
    if not i=="image_library.py": # pass gec
        im=Image.open(i).convert("CMYK") # resmi convert et
        im=im.filter(ImageFilter.FIND_EDGES) # kenar filtresi ekle
        im.save("boya_"+i) # kenarlari bulunan resim 'boya_' isminde tekrar kaydedildi



