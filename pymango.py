#!/usr/bin/python3

 

import pymongo



#mongodb account, database, table

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["ur database"]

mycol = mydb["dataset"]

#the whole table

print("the whole information in table first:") 

for x in mycol.find():

  print(x)

print("\n")



#show the information about account_id and picture number

print("the account id and picture number:")

for x in mycol.find({},{ "_id": 0, "account_id": 1, "picture": 1 }):

  print(x)

print("\n")



#search for a word

myquery = { "keyword": "nature" }

 

mydoc = mycol.find(myquery)

print("the information where keyword is nature:")

for x in mydoc:

  print(x)  

print("\n")



#most popular descriptors

print("the most popular descriptors:")

for x in mycol.find({},{'_id':0,'keyword':1}):

	print(x)

