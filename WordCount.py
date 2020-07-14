from operator import add

from pyspark.sql import SparkSession

spark = SparkSession\
.builder\
.appName("PythonWordCount")\
.getOrCreate()

f = "/Users/jagadeeshyadav/wordcount.txt"

lines = spark.read.text(f).rdd.map(lambda r:r[0])
counts = lines.flatMap(lambda x: x.split(' ')) \
.map(lambda x: (x, 1)) \
.reduceByKey(add)
#.reduceByKey(lambda  a, b : a + b)
counts.foreach(print)
