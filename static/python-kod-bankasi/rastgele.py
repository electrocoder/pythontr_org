#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        rastgele
# Purpose:     rastgele sayıların üretilmesi...
#
# Author:      electrocoder
#
# Created:     23/12/2011
# Copyright:   (c) electrocoder 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def main(sample_count):
    """10 adet test datasi uretir"""
    j=0
    test_data=[]
    while j < sample_count:
        test_data.append(random.random())
        j+=1
    print "data %s"%test_data
    return test_data

if __name__ == '__main__':
    main(10)
