from app.index import index
from pyspark.sql.functions import col
from pyspark.sql.functions import col, substr
from pyspark.sql.functions import substring

spark, url, properties, conn, cur, conn_admin, cur_admin = index()

users = spark.read.csv("/home/linux-adrian/Documents/pyspark/system/public/dev/pmol/python.csv", header=True, inferSchema=True)

users.count()

users.printSchema()

users.show(5, False)

users_drop = users.drop('No.', 'SCHEDTABLE', 'RUN AS', 'ORDER ID', 'RUN TIME', 'RUN COUNTER', 'HOST', 'CPUTIME')

users_drop.show(5, False)

users_drop.printSchema()

users_subs = users_drop.withColumn('ODATE', col('ODATE').cast('string'))

users_subs.printSchema()

users_filter = users_subs.withColumn('year', substring('ODATE', 1, 4))\
                         .withColumn('month', substring('ODATE', 5, 2))\
                         .withColumn('day', substring('ODATE', 7, 2))

users_filter.printSchema()

users_filter.show(5, False)

user_end = users_filter.drop('No.', 'SCHEDTABLE', 'RUN AS', 'ORDER ID', 'RUN TIME', 'RUN COUNTER', 'HOST', 'CPUTIME', 'ODATE')

user_end.show(5, False)

user_end.groupBy('JOBNAME').count().show(5, False)
