"""
Example modified from article:
https://towardsdatascience.com/using-kafka-to-optimize-data-flow-of-your-twitter-stream-90523d25f3e8
"""
import json
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from confluent_kafka import Producer
import logging

from config import kafka_config, twitter_config

logging.basicConfig(
   format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
   level=logging.DEBUG
)
log = logging.getLogger("TwitterStream")

def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    # else:
    #     sys.stderr.write('%% Message delivered to %s [%d] @ %o\n' % (msg.topic(), msg.partition(), msg.offset()))


class twitterAuth():
    """SET UP TWITTER AUTHENTICATION"""

    def authenticateTwitterApp(self):
        auth = OAuthHandler(twitter_config["consumer_key"], twitter_config["consumer_secret"])
        auth.set_access_token(twitter_config["access_token"], twitter_config["access_token_secret"])

        return auth


class TwitterStreamer():

    """SET UP STREAMER"""
    def __init__(self):
        self.twitterAuth = twitterAuth()

    def stream_tweets(self):
        while True:
            listener = ListenerTS()
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            stream.filter(track=track_list, stall_warnings=True, languages= ["en", "es"])


class ListenerTS(StreamListener):

    def on_data(self, raw_data):
            log.debug(raw_data)
            try:
                id = str.encode(json.loads(raw_data)['id_str'])
            except (KeyError, TypeError):
                id = None
            producer.produce(topic_name, str.encode(raw_data), key=id, callback=delivery_callback)
            producer.poll(2)
            return True


if __name__ == "__main__":
    producer = Producer(**kafka_config)
    topic_name = "tech_twitter"
    track_list = ["Azure", "AzureSynapse", "AzureDatabricks", "Databricks", "AzureDataLake", "AzureDataLakeGen2",
                  "AzureDataFactory", "HDInsight", "AzureIoT", "CosmosDB", "AzureSQL", "PowerBI", "ApacheSpark",
                  "ApacheKafka", "Confluent", "Airflow", "DataEngineering"]

    try:
        TS = TwitterStreamer()
        TS.stream_tweets()
    except Exception as err:
        producer.flush()
        raise err