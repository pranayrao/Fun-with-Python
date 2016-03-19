# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 13:10:30 2016

@author: pranay
"""

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positive=0
negative=0
zeroes=0
for i in arr:
    if i<0:
        negative+=1
    elif i > 0:
        positive+=1
    else:
        zeroes+=1
print float(positive)/n
print float(negative)/n
print zeroes/n