# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 23:00:43 2016

@author: pranay
"""

import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break
            fields = line.split(",")
            entry = {}            
            for i,value in  enumerate(fields):
                entry[header[i].strip()] = value.strip()
            data.append(entry)
            counter += 1
            
    print data
           
        
        
d = parse_file(DATAFILE)