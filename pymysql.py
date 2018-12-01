#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
db = pymysql.connect("localhost", "root", "ur password", "ur database", charset='utf8' )

# use cursor() to get action cursor 
cursor = db.cursor()

# use execute to SQL
cursor.execute("select VERSION()")

# use fetchone() gain data
data = cursor.fetchone()

# print ("Database version : %s " % data)

sql="select * from syt"
try:
	cursor.execute(sql) 	#run sql sentence
	results = cursor.fetchall()	#fetch all results
	print('The whole results is:')
	print(results)
	print('\n')
except:
   print ("Error: unable to fecth data")


sql = "select * from syt where keyword='nature'" 
try:
   # execute sql
   cursor.execute(sql)
   # Get a list of all records
   results = cursor.fetchall()
   print("details where keyword=nature" )
   print(results)

   print("\n")
except:
   print ("Error: unable to fecth data")



sql="select * from syt"

try:
    cursor.execute(sql) 	
    results = cursor.fetchall()
    print("number of picture")
    for row in results:
        username = row[0]
        twitter = row[1]
        number_of_pictures = row[2]
        location_of_pictures = row[3]
        video = row[4]
        keyword = row[5]
        
        print(("username=%s,number_of_pictures=%s") % \
        (username,number_of_pictures))
    print("\n")    
except:
   print ("Error: unable to fecth data")

#see most popular descriptors
sql="select keyword,count(*) as count from syt group by keyword order by count desc"
try:
	cursor.execute(sql) 	
	results = cursor.fetchall()
	print('the most popular description:')
	print(results)
	print("\n")

except:
   print ("Error: unable to fecth data")












# close database
db.close()