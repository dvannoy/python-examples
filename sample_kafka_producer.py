""" Simple kafka-python sample based on example at https://kafka-python.readthedocs.org/en/latest/usage.html
  * if not installed run 'pip install kafka-python' in terminal
  * if topic doesn't exist, must have kafka cluster setup to auto create topic or create it manually
  * if creating topic for first time, may receive an error on sending message, just run it again
  * if using AWS make sure server names are in your hosts file since it will return info on the brokers
"""
from kafka import KafkaClient, SimpleProducer, KeyedProducer, create_message
from kafka.common import ProduceRequest, FailedPayloadsError
from config import KAFKA_URL
import logging

logging.basicConfig(
   format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
   level=logging.WARN
)

kafka = KafkaClient(KAFKA_URL)
producer = SimpleProducer(kafka)
# send basic messages
try:
	producer.send_messages(b'python-sample-topic-1', b'test message 1')
	producer.send_messages(b'python-sample-topic-1', b'test message 2', b'test 3 additional message')
except FailedPayloadsError as e:
	print 'Simple Producer payload exception...'
	print e
#send keyed message
producer2 = KeyedProducer(kafka)
try:
	producer2.send_messages(b'python-sample-topic-1', b'key1', b'test keyed message 1')
except FailedPayloadsError as e:
	print 'Keyed Producer payload exception...'
	print e


# # To send messages asynchronously
# producer = SimpleProducer(kafka, async=True)
# producer.send_messages(b'my-topic', b'async message')

# # To wait for acknowledgements
# # ACK_AFTER_LOCAL_WRITE : server will wait till the data is written to
# #                         a local log before sending response
# # ACK_AFTER_CLUSTER_COMMIT : server will block until the message is committed
# #                            by all in sync replicas before sending a response
# producer = SimpleProducer(kafka, async=False,
#                           req_acks=SimpleProducer.ACK_AFTER_LOCAL_WRITE,
#                           ack_timeout=2000,
#                           sync_fail_on_error=False)

# responses = producer.send_messages(b'my-topic', b'another message')
# for r in responses:
#     logging.info(r.offset)

# # To send messages in batch. You can use any of the available
# # producers for doing this. The following producer will collect
# # messages in batch and send them to Kafka after 20 messages are
# # collected or every 60 seconds
# # Notes:
# # * If the producer dies before the messages are sent, there will be losses
# # * Call producer.stop() to send the messages and cleanup
# producer = SimpleProducer(kafka, async=True,
#                           batch_send_every_n=20,
#                           batch_send_every_t=60)

