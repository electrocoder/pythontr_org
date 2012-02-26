#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        python & numpy & matplotlib kullanımı
# Purpose:     rastgele sayılardan oluşan grafigin python ve matplot ile
#              çizdirilmesi...
#
# Author:      electrocoder
#
# Created:     23/12/2011
# Copyright:   (c) electrocoder 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pylab import *
from Tkinter import *
import matplotlib.pyplot as plt
from time import gmtime, strftime
import rastgele

def plot_1(t_data):
    """random sayılardan oluşan 1 nolu plot çizimi"""
    plt.figure(1)
    plt.subplot(211)
    plt.title("Urun toplami " + strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
    #test data start
    j=[]
    for jj in range(len(t_data)):
        j.append(jj/10.0)
    print j
    plt.plot(j,t_data, 'r')
    #test data stop
    ylabel("Agirlik (kg)")
    grid(True)

def plot_2(t_data):
    """random sayılardan oluşan 2 nolu plot çizimi"""
    plt.figure(1)
    plt.subplot(212)
    plt.title("Urun toplami " + strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
    #test data start
    j=[]
    for jj in range(len(t_data)):
        j.append(jj/10.0)
    plt.plot(j,t_data, 'b')
    #test data stop
    xlabel("Zaman (yil)")
    ylabel("Agirlik (kg)")
    grid(True)

def main():
    """plot ve random kullanım orneği"""
    plot_1(rastgele.main(20))
    plot_2(rastgele.main(50))
    printer()
    plt.show()

def printer():
    """cizim sonucunu pdf olarak kaydeder"""
    savefig("grafik.pdf")

if __name__ == '__main__':
    main()
