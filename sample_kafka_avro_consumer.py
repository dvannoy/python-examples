""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
and also used example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/.
  * enter topic as parameter when running script (ex. python sample_kafka_consumer.py python-sample-topic-1)
  * if not installed run 'pip install kafka-python' in terminal
  * if using AWS make sure server names are in your hosts file since it will return info on the brokers
"""
from kafka import KafkaClient, SimpleConsumer, KafkaConsumer
import avro.schema
import avro.io
import io
from sys import argv
from config import KAFKA_URL

topic = argv[1] #enter topic as parameter when running script
schema_path = argv[2] # enter schema path as parameter when running script

schema = avro.schema.parse(open(schema_path, 'rb').read())
using_schema_registry = False

consumer = KafkaConsumer(topic, topic+"sample-group",bootstrap_servers=[KAFKA_URL])
consumer.max_buffer_size=0
for message in consumer:
    if using_schema_registry:
        # Leave off first 5 characters if using confluent schema registry and avro encoder when creating message
        # The first 5 characters were meant to indicate the schema version to be looked up in the registry
        # More detail here: https://groups.google.com/forum/#!topic/confluent-platform/A7B6uSnJa5k
        bytes = io.BytesIO(message.value[5:])
    else:
        bytes = io.BytesIO(message.value)
    decoder = avro.io.BinaryDecoder(bytes)
    reader = avro.io.DatumReader(schema)
    decoded_message = reader.read(decoder)
    print message.offset
    print decoded_message

