# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 13:55:28 2016

@author: pranay
"""

#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
zipfile = "2013_ERCOT_Hourly_Load_Data"
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(zipfile), 'r') as myzip:
             myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    ### example on how you can get the data
    coast = sheet.col_values(1,start_rowx=1)
    maxrowno=0
    maxvalue=0
    minvalue=sheet.cell_value(0,1)
    rowno=0
    for values in coast:
                
        if values > maxvalue:
            maxvalue = values
            maxrowno = rowno+1
        
        if values < minvalue:
            minvalue=values
            minrowno= rowno+1
        rowno+=1  
    
    maxvalue = sheet.cell_value(maxrowno,1)    
    maxexceltime = sheet.cell_value(maxrowno,0)
    maxtime = xlrd.xldate_as_tuple(maxexceltime,0)
    avgcoast = sum(coast)/len(coast)    
    minvalue = sheet.cell_value(minrowno,1)
    minexceltime = sheet.cell_value(minrowno,0)
    mintime = xlrd.xldate_as_tuple(minexceltime,0)
#    print maxvalue,minvalue,avgcoast,maxtime,mintime
    
    
    
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    #coast=[]    
    #for records in sheet_data:
    #     coast.append(records[1])
    #coast = coast[1:])
    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    data = {
            'maxtime': maxtime,
            'maxvalue': maxvalue,
            'mintime': mintime,
            'minvalue': minvalue,
            'avgcoast': avgcoast
    }
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()