from pyspark import SparkContext
from pyspark.sql import SQLContext
import traceback
import MySQLdb
import datetime

db = MySQLdb.connect("localhost","root","iiita","analytics")
cursor = db.cursor()

sc = SparkContext("local", "temperature")
sqlContext = SQLContext(sc)
lines = sc.textFile("enigma.csv")

#def funct(key, events):


parts = lines.map(lambda l: l.split(","))
users = parts.map(lambda p: (p[0],p[5]))

records = users.groupByKey()

sum = 0
count = 0

for val in records.collect() :
	sum = 0
	count = 0
	for val1 in val[1]:
		count = count + 1
		sum = sum + float(val1)
	avg = sum/count
	print avg
	sql = "INSERT INTO max_temperature (date,max_temp) VALUES ('%s','%f')" % ((val[0]),(avg))
	try:
		cursor.execute(sql)
		db.commit()
	except Exception, err:
		traceback.print_exc()
		db.rollback()
db.close()


	