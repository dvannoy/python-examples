""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
and also used example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/.
  * enter topic as parameter when running script (ex. python sample_kafka_consumer.py python-sample-topic-1)
  * if not installed run 'pip install kafka-python' in terminal
  * if using AWS make sure server names are in your hosts file since it will return info on the brokers
"""
#from kafka import KafkaClient, SimpleConsumer, KafkaConsumer
from confluent_kafka import Consumer, KafkaError
from sys import argv
from config import KAFKA_URL
import logging

logging.basicConfig(
   format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
   level=logging.WARN
)

topic = argv[1] #enter topic as parameter when running script
group = "sample-group-1" #only use if trying to consume in parallel
#group = None
if len(argv) > 2 and argv[2] == 'reset':
    #auto_offset_reset = 'earliest'
    auto_offset_reset = 'smallest'
else:
    auto_offset_reset = 'latest'

consumer = Consumer({'bootstrap.servers': KAFKA_URL, 'group.id': group,
              'default.topic.config': {'auto.offset.reset': auto_offset_reset}})
consumer.subscribe([topic])

running = True
while running:
    message = consumer.poll()
    if not message.error():
        print('Received message: %s' % message.value().decode('utf-8'))
        #print str(message[4])
    elif message.error().code() != KafkaError._PARTITION_EOF:
        print(message.error())
        running = False
consumer.close()

