# started with example at http://www.makedatauseful.com/kafka-consumer-simple-python-script-and-tips/
# need to pip install kafka-python
from kafka import KafkaClient, SimpleConsumer
from sys import argv
from config import KAFKA_URL

kafka = KafkaClient("KAFKA_URL:6667")
consumer = SimpleConsumer(kafka, "sample-group", argv[1])
consumer.max_buffer_size=0
consumer.seek(0,2)
for message in consumer:
 print("OFFSET: "+str(message[0])+"\t MSG: "+str(message[1][3]))
