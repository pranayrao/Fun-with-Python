# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 14:32:53 2016

@author: pranay
"""

import sys


n = int(raw_input().strip())
j = n-1
i=1
while i <= n and j>=0:
    print (" "*j+"#"*i)
    i+=1
    j-=1