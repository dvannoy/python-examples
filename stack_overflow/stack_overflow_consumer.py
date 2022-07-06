import json
import sys
import time
import requests
from confluent_kafka import Producer
import logging

from config import kafka_config


logging.basicConfig(
   format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
   level=logging.DEBUG
)
log = logging.getLogger("TwitterStream")


def get_questions(endpoint, fromdate, todate):
    tags = "pyspark;apache-spark-sql" # post must match all tags
    query_string = f"?fromdate={str(fromdate)}&todate={str(todate)}&order=desc&min=1&sort=votes&tagged={tags}&filter=default&site=stackoverflow&run=true" #tagged=python&site=stackoverflow"
    r = requests.get(f"{endpoint}{query_string}")
    if r.status_code == 200:
        return r.text
    else:
        return r

def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)

def send_to_kafka(topic, records):
    producer = Producer(**kafka_config)
    for msg in records:
        try:
            id = str.encode(str(msg["question_id"]))
        except (KeyError, TypeError):
            id = None
        producer.produce(topic, str.encode(json.dumps(msg)), key=id, callback=delivery_callback)
        producer.poll(2)

if __name__ == "__main__":
    topic_name = "stackoverflow_questions"
    endpoint = "https://api.stackexchange.com/2.2/questions"
    todate = int(time.time()) - 18000  # test value: "1619178204"
    fromdate = todate - 100000  # test value: "1617108204"

    response = get_questions(endpoint, fromdate, todate)
    response_json = json.loads(response)
    question_list = response_json["items"]
    log.debug(f"fromdate={fromdate}, todate={todate}")
    log.debug(question_list)

    # Remove items and print response metadata
    del response_json["items"]
    metadata = response_json
    log.info(f"API metadata: {metadata}")

    # Produce records in list to Kafka
    send_to_kafka(topic_name, question_list)


