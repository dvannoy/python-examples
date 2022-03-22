""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
and also used example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/.
  * enter topic as parameter when running script (ex. python sample_kafka_consumer.py python-sample-topic-1)
  * if not installed run 'pip install kafka-python' in terminal
  * if using AWS make sure server names are in your hosts file since it will return info on the brokers
"""
#from kafka import KafkaClient, SimpleConsumer, KafkaConsumer
from confluent_kafka import Consumer, KafkaError
from sys import argv
from config import kafka_config
import logging

logging.basicConfig(
   format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
   level=logging.WARN
)

topic = "tech_twitter" # argv[1] #enter topic as parameter when running script
group = "sample-group-1" #only use if trying to consume in parallel

if len(argv) > 2 and argv[2] == 'reset':
    auto_offset_reset = 'smallest'
else:
    auto_offset_reset = 'latest'

kafka_config["group.id"] = group
kafka_config["default.topic.config"] = {'auto.offset.reset': auto_offset_reset}

consumer = Consumer(kafka_config)
consumer.subscribe([topic])

running = True
while running:
    message = consumer.poll()
    if not message.error():
        print(message.value().decode('utf-8'))
    elif message.error().code() != KafkaError._PARTITION_EOF:
        print(message.error())
        running = False
consumer.close()

