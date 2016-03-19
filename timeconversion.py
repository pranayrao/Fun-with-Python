# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 20:07:31 2016

@author: pranay
"""

intime = raw_input().strip()
hh=(intime[:2])
hh=int(hh)
AM_PM=intime[-2:]
time = intime[:-2]
if AM_PM=='AM':
    if hh==12:
        new_hh=hh-12
        print (str(new_hh)*2)+time[2:]
    else:
        print time
elif AM_PM=='PM':
    if hh>=1 and hh<=11:
        new_hh=hh+12
        print str(new_hh)+time[2:]
    else:
        print time