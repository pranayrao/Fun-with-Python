import glob
import pymongo
import re
import time

# function to record current time in milliseconds
current_time = lambda: int(round(time.time() * 1000))

# establish connection with mongodb
connection = pymongo.MongoClient("mongodb://localhost",port=27011)
db = connection.mgs618

# define collection
sf = db.sf

# read data from all text files present in current working directory
filelist = glob.glob('./*.txt')

# delete data if it already exists
db.sf.delete_many({})

# delete results if it already exists
db.final_result.delete_many({})

# read data for each file
for file in filelist:

    data = open(file).read()
# remove underscore
    nosp = re.sub('_+',' ',data)
# remove any non word characters
    plaintext = re.sub('\W+', ' ', nosp)
# remove numbers and convert to lowercase
    text = re.sub('\d',' ',plaintext).lower()
# insert into mongodb collection
    db.sf.insert({"text":text})


# call javascript containing map function
map = open("map.js","r").read()

# call javascript containing reduce function
reduce = open("reduce.js","r").read()

# capture begin time
start_time = current_time()

# map-reduce in mongodb
result = db.sf.map_reduce(map, reduce,"final_result")

# capture end time
end_time = current_time()

# calculate and print time taken for map reduce
duration = end_time - start_time
print "Time taken:"+str(duration)+" ms"

# print result
print "This collection has:"
for doc in result.find():
   print str(int(doc["value"]["count"])),str(int(doc["_id"]))+"-letter_word(s)"
