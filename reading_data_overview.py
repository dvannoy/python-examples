import json
from urllib import urlopen

import paramiko
import requests


def read_json_newlines_local(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data


def read_json_local(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def read_json_newlines_http(file):
    data = []
    for line in urlopen(file):
        data.append(json.loads(line.decode('utf-8')))
    return data

def read_json_http():
    r = requests.get(
        'https://pkgstore.datahub.io/core/house-prices-us/cities_json/data/fdb183dfcd2ac5b1525f4b1ca2634880/cities_json.json')
    data = r.json()
    return data


def write_json(data, outfile):
    with open(outfile, 'w') as fileout:
        json.dump(data, fileout)


def average_age(lst):
    sum = 0
    ages = [x["subject_age"] for x in lst if 'subject_age' in x]
    cnt = len(ages)
    for i in ages:
        try:
            sum += int(i)
        except ValueError as e:
            cnt = cnt-1
    return sum/cnt

def read_json_remote_server():
    filename = 'vehicle_stops_sample.json'
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.connect('localhost', username='user', key_filename='/Users/sample_user/.ssh/ssh_key')

    sftp_client = ssh_client.open_sftp()
    with sftp_client.open(filename) as remote_file:
        data = []
        for line in remote_file:
            data.append(line.strip('\n'))
    return data


def read_postgres(user, password, host, database):
    from sqlalchemy import create_engine

    engine = create_engine("postgres://{0}:{1}@{2}/{3}".format(user, password, host, database))
    connection = engine.connect()
    query = "select * from test_table"
    result = connection.execute(query)
    return result

if __name__=='__main__':

    json_file = 'data/vehicle_stops.json'  # valid json object that is an array of vehicle stop records
    json_records_file = 'data/vehicle_stops_newline_delimited.json'  # newline delimited json file of vehicle stop records
    s3_file = 'https://s3-us-west-2.amazonaws.com/dvannoy-public/sample_data/vehicle_stops_newline_delimited.json'

    # Each of these lines will read data
    #data = read_json_newlines_local(json_records_file)
    #data = read_json_http()
    data = read_json_newlines_http(s3_file)
    # data = read_json_local(json_file)

    print(data[0:5])  # print top 5 rows
    # print(json.dumps(data, indent=2))
    # print("Average age: %s" % average_age(data))

    # Read using ssh
    # read_json_remote_server()

    # Read from postgres
    # user = 'postgres'
    # password = ''
    # host = 'localhost'
    # database = 'postgres'
    # read_postgres(user, password, host, database)
