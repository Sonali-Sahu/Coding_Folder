from pyspark.sql import SparkSession
# start a session 
spark = SparkSession.builder.appName("GL_SparkSQL").getOrCreate()
spark
# schema inference example
# spark call 
sc = spark.sparkContext
text_df = sc.textFile('textfile.txt')
text_df.collect()
lines = text_df.filter(lambda x:x!=" ")
words_df = lines.flatMap(lambda x:x.split(" "))
words_df.collect()
words_counts = words_df.map(lambda x:(x,1))
word_counts = words_counts.reduceByKey(lambda x, y: x + y)
word_counts.collect()
