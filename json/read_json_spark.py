from pyspark.sql import SparkSession, functions

path = "/data1/tmp/plan.json"

spark = SparkSession.builder.appName("Read Json").getOrCreate()

df = spark.read.json(path)

df2 = df.select("Name", "CreatedOn", "Admins")
df3 = df2.select("Name", "CreatedOn", functions.explode(df2.Admins).alias("Adm")).groupBy("Name", "CreatedOn").count()

print(df3.show())