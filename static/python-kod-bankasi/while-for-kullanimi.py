#-*- coding:utf-8 -*-
#Programin amaci;
#while ve for kullanimi

print "Öğrenci Takip Programı"

ogrenciAdi=[]
ogrenciSoyadi=[]
ogrenciNo=[]
soru='e'

while soru=='e':
    ogrenciAdi.append(raw_input("Ogrencinin Adini Giriniz"))
    ogrenciSoyadi.append(raw_input("Ogrencinin Soyadini Giriniz"))
    ogrenciNo.append(raw_input("Ogrencinin Nosunu Giriniz"))
    soru=raw_input("Eklemek icin 'e', Liste icin 'l'")

for i in range(len(ogrenciAdi)):
    print ogrenciAdi[i], ogrenciSoyadi[i], ogrenciNo[i]

print "İyi çalışmalar..."


