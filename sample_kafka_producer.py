# started with example at https://kafka-python.readthedocs.org/en/latest/usage.html
# need to pip install kafka-python
from kafka import KafkaClient, SimpleProducer
from sys import argv
from config import KAFKA_URL

kafka = KafkaClient(KAFKA_URL)
producer = SimpleProducer(kafka)
producer.send_messages(b'sample-topic-1', b'test message 1')
producer.send_messages(b'sample-topic-1', b'test message 2', b'etc')



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

