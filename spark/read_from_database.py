from pyspark import SparkContext
from pyspark.sql import SparkSession

POSTGRES_HOST = 'localhost'
POSTGRES_USER = 'postgres'
POSTGRES_DB = 'postgres'
POSTGRES_PASSWORD = ''


def load_from_postgres(table):
    spark = SparkSession.builder.appName("read_from_postgres").getOrCreate()

    df = spark.read.format("jdbc").options(
        source="jdbc",
        url="jdbc:postgresql://{0}:5432/{1}".format(POSTGRES_HOST, POSTGRES_DB),
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbtable=table).load()

    return df


def write_to_postgres(df, table, mode = 'append'):
    db_properties = {
        "user": POSTGRES_USER,
        "password": POSTGRES_PASSWORD
    }

    df.write.jdbc(
        url="jdbc:postgresql://{0}:5432/{1}".format(POSTGRES_HOST, POSTGRES_DB),
        properties = db_properties,
        table=table,
        mode = mode)

table = "vehicle_stops"
df = load_from_postgres(table)
print(df.show())
target_table = "vehicle_stops2"
write_to_postgres(df, target_table)