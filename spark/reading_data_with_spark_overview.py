from pyspark import SparkContext
from pyspark.sql import SparkSession, functions, types
from config.config import SPARK_PROPERTIES, POSTGRES_HOST, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER
import os

# For Postgres source
SUBMIT_ARGS = "--master local[4] --driver-class-path /opt/jdbc/postgresjdbc/postgresql-42.1.1.jar --driver-memory 8g --executor-memory 8g pyspark-shell"
os.environ["PYSPARK_SUBMIT_ARGS"] = SUBMIT_ARGS

def process_json_records(file):
    spark = SparkSession.builder.appName("Reading Overview").getOrCreate()

    df = spark.read.json(file)

    print(df.show())
    # print(json.dumps(data, indent=2))
    #df_avg = df.select("subject_age", df.subject_age.cast(IntegerType()).alias("ages")).agg(avg("subject_age").alias("avg_age"))
    df_avg = df.agg(functions.avg("subject_age"))

    print("Average age: %s" % df_avg.first()[0])


def process_json(file):
    spark = SparkSession.builder.appName("Reading Overview").getOrCreate()

    df = spark.read.json(file)

    print(df.show())

    # print(json.dumps(data, indent=2))
    df_avg = df.agg(functions.avg("subject_age"))
    print("Average age: %s" % df_avg.first()[0])


def process_json_records_s3(file):
    spark = SparkSession.builder.appName("Reading Overview").getOrCreate()
    df = spark.read.json(file)

    print(df.show())
    df_avg = df.agg(functions.avg("subject_age"))
    print("Average age: %s" % df_avg.first()[0])


def load_from_postgres():
    """ Read from json files, write to different json files, show first 20 records
        *takes about 2 minutes for month of April
    """
    spark = SparkSession.builder.appName("postgres_read").getOrCreate()

    filter = ""
    table = """(select *
                from test {0}) cv""".format(filter)

    df = spark.read.format("jdbc").options(
        source="jdbc",
        url="jdbc:postgresql://{0}:5432/{1}".format(POSTGRES_HOST, POSTGRES_DB),
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbtable=table).load()

    ## write to a json file
    # df.write.option("compression", "none").mode("overwrite").json(
    #     "file:///User/sample_user/output")

    return df


if __name__=='__main__':

    # Local Json Files
    json_file = 'data/vehicle_stops.json'  # valid json object that is an array of vehicle stop records
    json_records_file = 'data/vehicle_stops_newline_delimited.json'  # newline delimited json file of vehicle stop records

    process_json_records(json_records_file)
    # process_json(json_file)


    # S3 example - sort of
    s3file='s3n://{0}:{1}@dvannoy-public/sample_data/vehicle_stops_newline_delimited.json'.format(
            SPARK_PROPERTIES['access_key'], 'AFSDFE')
    # process_json_records_s3(s3file)

    # Postgres
    #load_from_postgres()
