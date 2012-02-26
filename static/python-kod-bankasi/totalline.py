#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#-------------------------------#
#    Coded by h4ckinger    #
#    www.h4ckinger.org    #
#    h4ckinger@gmail.com    #
#-------------------------------#
 
import sys,os
from mimetypes import guess_type
 
def list_files(directory):
    """ Lists files in directory from parameter """
    for root, dirs, files in os.walk(directory):
        for x in files:
            dsy = os.path.join(root,x)
            tip = guess_type(dsy)[0]
            if tip and tip.split("/")[0] == "text":
                yield dsy
 
def main():
    directory = sys.argv[1] if len(sys.argv)>1 else "."
    total = 0
    total_file = 0
    for dosya in list_files(directory):
        count = len(open(dosya).readlines())
        print "%s:%s " % (os.path.basename(dosya),count)
        total+= count
        total_file+= 1
 
    print "total %s file and %s lines" % (total_file, total)
 
if __name__ == "__main__" :
    main()
