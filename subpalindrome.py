# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 15:26:38 2016

@author: pranay
"""
string = raw_input().strip()
s=[]
for i in range(len(string)):
	j = i
	while j < len(string):
            if string[i:j+1] not in s:
                s.append(string[i:j+1])
            j+=1
counter=0
sub = s
for i in sub:
        if i == i[::-1]:
                 counter+=1
print counter
        