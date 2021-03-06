""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
and also used example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/.
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
#group = "sample-group-1" #only use if trying to consume in parallel
group = None
if len(argv) > 2 and argv[2] == 'reset':
    auto_offset_reset = 'earliest'
else:
    auto_offset_reset = 'latest'

try:
    consumer = KafkaConsumer(topic, group_id=group, bootstrap_servers=[KAFKA_URL], auto_offset_reset=auto_offset_reset)
    #consumer.subscribe([topic])
    consumer.max_buffer_size=0
    for message in consumer:
        #print message.encode('utf-8')
        #print("OFFSET: " + str(message[3]) + "\t KEY: " + str(message[3]) + "\t MSG: " + str(message[4]))
        print str(message[4])
except Exception as e:
    print 'Error in consumer...'
    print e
