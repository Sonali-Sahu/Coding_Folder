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

output:- 
[('of', 2),
 ('', 2),
 ('When', 1),
 ('we', 1),
 ('feel', 1),
 ('neglect', 1),
 ('However,', 1),
 ('help', 1),
 ('sure', 1),
 ("you're", 1),
 ('eating', 1),
 ('healthy', 1),
 ('getting', 1),
 ('sleep,', 1),
 ('in', 1),
 ('regular', 1),
 ('exercise.', 1),
 ('Take', 1),
 ('care', 2),
 ('your', 3),
 ('physical', 2),
 ('health', 1),
 ('down,', 1),
 ("it's", 1),
 ('easy', 1),
 ('to', 1),
 ('our', 1),
 ('needs.', 1),
 ('taking', 1),
 ('body', 1),
 ('can', 1),
 ('boost', 1),
 ('mood', 1),
 ('and', 2),
 ('energy', 1),
 ('levels.', 1),
 ('Make', 1),
 ('a', 1),
 ('diet,', 1),
 ('enough', 1),
 ('engaging', 1)]
