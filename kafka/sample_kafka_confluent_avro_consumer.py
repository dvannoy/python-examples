""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
and also used example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/.
  * enter topic as first parameter when running script (ex. python sample_kafka_consumer.py python-sample-topic-1)
  * enter "reset" as second parameter to reprocess all available messages
  * if not installed run 'pip install kafka-python' in terminal
  * if using AWS make sure server names are in your hosts file since it will return info on the brokers
"""
from kafka import KafkaClient, SimpleConsumer, KafkaConsumer
import avro.schema
import avro.io
import io
import time
from confluent.schemaregistry.client import CachedSchemaRegistryClient
from confluent.schemaregistry.serializers import MessageSerializer
from sys import argv
from config import KAFKA_URL, SCHEMA_REGISTRY_URL

kafka_brokers = KAFKA_URL
schema_registry = SCHEMA_REGISTRY_URL

topic = argv[1] #enter topic as parameter when running script
if len(argv) > 2 and argv[2] == 'reset':
    auto_offset_reset = 'smallest'
else:
    auto_offset_reset = 'largest'

schema_registry_client = CachedSchemaRegistryClient(url=schema_registry)
serializer = MessageSerializer(schema_registry_client)

# simple decode to replace Kafka-streaming's built-in decode decoding UTF8 ()
def decoder(s):
    decoded_message = serializer.decode_message(s)
    return decoded_message

timestamp = time.time()

consumer = KafkaConsumer(topic, "sample-group-"+str(timestamp), bootstrap_servers=[kafka_brokers], auto_offset_reset=auto_offset_reset)
consumer.max_buffer_size=0
for message in consumer:
    decoded_message = decoder(message.value)
    print message.offset
    print decoded_message
