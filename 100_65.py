# coding: utf-8
import gzip
import json
import leveldb
import pymongo

fname = 'artist.json.gz'
fname_db = 'test_db'
client=pymongo.MongoClient(host='localhost', port=27017)

mongo_db=client.mongo
mongo_db.collection1
collection=mongo_db.collection1


#with gzip.open(fname, 'rt') as data_file:
    for line in data_file:
        data_json = json.loads(line)
        #每个data_file如果list内值多于一就复制值的数量的分身，然后每个分配一个list使其成为单值
        collection.insert_one(data_json)
      

collection.create_index([("name",pymongo.ASCENDING),("rating.value",pymongo.ASCENDING)])

result=collection.find_one({"name":'Queen'})
print (result)
