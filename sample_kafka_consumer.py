""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
and also used example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/
  * enter topic as parameter when running script (ex. python sample_kafka_consumer.py python-sample-topic-1)
  * if not installed run 'pip install kafka-python' in terminal
  * if using AWS make sure server names are in your hosts file since it will return info on the brokers
"""
from kafka import KafkaClient, SimpleConsumer, KafkaConsumer
from sys import argv
from config import KAFKA_URL
import logging

logging.basicConfig(
   format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
   level=logging.WARN
)

topic = argv[1] #enter topic as parameter when running script

try:
    consumer = KafkaConsumer(topic, "sample-group1",bootstrap_servers=[KAFKA_URL])
    consumer.max_buffer_size=0
    for message in consumer:
        print("OFFSET: " + str(message[3]) + "\t KEY: " + str(message[3]) + "\t MSG: " + str(message[4]))
except Exception as e:
    print 'Error in consumer...'
    print e