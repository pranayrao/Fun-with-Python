runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
# *** Spyder Python Console History Log ***
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')
%clear
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')

##---(Sun Feb 28 01:52:06 2016)---
a
a=[1,2,3]
a
for i in a:    print i    
runfile('C:/Users/pranay/.spyder2/Udacity-Data Wrangling/untitled1.py', wdir='C:/Users/pranay/.spyder2/Udacity-Data Wrangling')

##---(Tue Mar 01 07:02:51 2016)---
list1 = [{key1:1,key2:2,key3:[{name:"p",age:27,weight:75},{name:"s",age:25,weight:57}]}]
list1 = [{'key1':1,'key2':2,'key3':[{name:"p",age:27,weight:75},{name:"s",age:25,weight:57}]}]
list1 = [{'key1':1,'key2':2,'key3':[{'name':"p",'age':27,'weight':75},{'name':"s",'age':25,'weight':57}]}]
list1
list1[0]
for l in list1:    print l[0]    
l for l in list1[0]
[l for l in list1[0]]
list1
for l in list1:    print l    
[l for l in list1]
list1
[l for l in list1[1]]
list1.index()
list1.getindex()
list1.index?
list1.count
list1.count()
list1.count?
list1.__len__
len(list1)
list1
%clear
[l for l in list1]
[l for l in list1[0]]
list2 =[{'key1': 1,  'key2': 2,  'key3': [{'age': 27, 'name': 'p', 'weight': 75},   {'age': 25, 'name': 's', 'weight': 57}]},{'male':300,"female":340}]
[l for l in list2[0]]
[l for l in list2[1]]
[l for l in list2]
[l for l in list2[0]]
[l['key3'] for l in list2[0]]
[l for l in list2[0]['key3']]
[l['weight'] for l in list2[0]['key3']]
result ='?max_id=313519052523986943&q=NCAA&include_entities=1'
result
for i in result[1:].split('&'):    print i.split('=')    
dict([print i.split('=') for i in result[1:].split('&')])
dict([i.split('=') for i in result[1:].split('&')])

##---(Wed Mar 02 02:34:56 2016)---
results = '?max_id=313519052523986943&q=NCAA&include_entities'
for kv in unquote(results[1:]).split('&'):    print kv    
for kv in results[1:].split('&'):    print kv    
for kv in results[1:].split('&'):    print kv.split('=')    
[kv.split('=') for kv in results[1:].split('&')] 
dict([kv.split('=') for kv in results[1:].split('&')])
d = dict([kv.split('=') for kv in results[1:].split('&')])
results = '?max_id=313519052523986943&q=NCAA&include_entities=1'
d = dict([kv.split('=') for kv in results[1:].split('&')])
d
l = [kv.split('=') for kv in results[1:].split('&')]
print type(l)
for (k,v) in l:    print k,v    
for (k,v) in l:    print k:v
{(k:v) for (k,v) in l}
{k:v for (k,v) in l}
list1
list2
%clear
dict1
%clear
key3
l1
%clear
[l['key3'] for l in list2[0]]
list2 =[{'key1': 1,  'key2': 2,  'key3': [{'age': 27, 'name': 'p', 'weight': 75},   {'age': 25, 'name': 's', 'weight': 57}]},{'male':300,"female":340}]
[l['key3'] for l in list2[0]]
list2
list2[0]
list2[0][0]
list2
%clear
list2
[l['weight'] for l in list2[0]['key3']]
runfile('C:/Training/Web Scraping with Python/ScrapeTest.py', wdir='C:/Training/Web Scraping with Python')

##---(Tue Mar 15 02:01:47 2016)---
runfile('C:/Users/pranay/JSON_to_CSV.py', wdir='C:/Users/pranay')