""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
and also used example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/.
  * enter topic as parameter when running script
  * enter schema registry url as second parameter when running script
  * if not installed run 'pip install kafka-python' in terminal
  * if using AWS make sure server names are in your hosts file since it will return info on the brokers
"""
from kafka import KafkaClient, SimpleConsumer, KafkaConsumer
import avro.schema
import avro.io
import io
from confluent.schemaregistry.client import CachedSchemaRegistryClient
from confluent.schemaregistry.serializers import MessageSerializer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from sys import argv
from config import KAFKA_URL, KAFKA_BROKER_LIST

topic = argv[1] #enter topic as parameter when running script
schema_registry_url = argv[2] # enter schema registry url (ex. http://localhost:8081)
if len(argv) > 3 and argv[3] == 'reset':
    auto_offset_reset = 'smallest'
else:
    auto_offset_reset = 'largest'

schema_registry_client = CachedSchemaRegistryClient(url=schema_registry_url)
serializer = MessageSerializer(schema_registry_client)

# simple decode to replace Kafka-streaming's built-in decode decoding UTF8 ()
def decoder(s):
    decoded_message = serializer.decode_message(s)
    return decoded_message

# Spark Streaming from Kafka
master = 'local[2]'
app_name = 'kafka_consumer'
sc = SparkContext(master, app_name)
ssc = StreamingContext(sc, 60)
kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": KAFKA_BROKER_LIST, "auto.offset.reset": auto_offset_reset}, valueDecoder=decoder)

lines = kvs.map(lambda x: x[1])
lines.pprint()
lines.saveAsTextFiles('consumed_data')

ssc.start()
ssc.awaitTermination()
