# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 13:26:15 2016

@author: pranay
"""

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
primary = 0
for i in range(n):
    primary = primary + a[i][i]
#print primary
secondary=0
i=n-1
j=0
while i>=0 and j<n:
        secondary= secondary+ a[i][j]
        i-=1
        j+=1
#print secondary
print abs(primary-secondary)


