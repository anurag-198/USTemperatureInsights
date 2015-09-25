from pyspark import SparkContext
from pyspark.sql import SQLContext
import traceback
import MySQLdb
import datetime


#connect to database "analytics"

db = MySQLdb.connect("localhost","root","iiita","analytics")

#getting a cursor to the selected area

cursor = db.cursor()

#reading the csv file

sc = SparkContext("local", "temperature")
sqlContext = SQLContext(sc)
lines = sc.textFile("enigma.csv")

#apply map reduce operations in the csv file


parts = lines.map(lambda l: l.split(","))
users = parts.map(lambda p: (p[0],p[6]))

#group by key which is the date

records = users.groupByKey()

sum = 0
count = 0

#calculating average 

for val in records.collect() :
	sum = 0
	count = 0
	for val1 in val[1]:
		count = count + 1
		sum = sum + float(val1)
	avg = sum/count
	print avg
#inserting the values in required table
	sql = "INSERT INTO minimum_temp (date,minimum_temp) VALUES ('%s','%f')" % ((val[0]),(avg))
	try:
		cursor.execute(sql)
		db.commit()
	except Exception, err:
		traceback.print_exc()
		db.rollback()
db.close()


	