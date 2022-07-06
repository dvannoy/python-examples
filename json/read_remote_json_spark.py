import base64
import json

import paramiko
from pyspark import SparkContext
from pyspark.sql import SparkSession
from config import key

ip = '172.0.0.1'

def read_remote_json_newline_delimited(ssh_client, filename):
    sftp_client = ssh_client.open_sftp()
    with sftp_client.open(filename) as remote_file:
         data = []
         for line in remote_file:
             data.append(line.strip('\n'))
    return data


def read_remote_json(ssh_client, filename):
    sftp_client = ssh_client.open_sftp()
    with sftp_client.open(filename) as remote_file:
        data = json.load(remote_file)
    return data

def spark_processing(data):
    sc = SparkContext()
    spark = SparkSession.builder.master("local").appName("Sample App").getOrCreate()
    # df = spark.createDataFrame(data)

    # if not using json.loads() upstream then try...
    rdd = sc.parallelize(data)
    df = spark.read.json(rdd)

    df.show()


if __name__ == "__main__":
    #filename = 'vehicle_stops_2016_datasd_clean_json/part-00000-b7691d0c-2052-4892-887a-19bf1b29cf1e.json'
    filename = 'vehicle_stops_sample.json'
    #filename = 'test.json'
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.connect(ip, username='dvannoy', key_filename='/Users/dustinvannoy/.ssh/dvannoy')

    data = read_remote_json_newline_delimited(ssh_client, filename)

    print(data)
    spark_processing(data)