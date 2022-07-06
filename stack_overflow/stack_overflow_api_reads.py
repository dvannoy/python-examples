import json
import time
import requests
import logging


logging.basicConfig(
   format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
   level=logging.DEBUG
)
log = logging.getLogger(__name__)


def get_questions(endpoint, fromdate, todate, tags=["apache-spark","pyspark"]):
    """Read first page of questions from Stack Overflow"""
    tags_str = ";".join(tags) # post must match all tags
    query_string = f"?fromdate={str(fromdate)}&todate={str(todate)}&order=desc&sort=activity&tagged={tags_str}&pagesize=100&filter=default&site=stackoverflow&run=true" #tagged=python&site=stackoverflow"
    r = requests.get(f"{endpoint}{query_string}")
    if r.status_code == 200:
        return r.text
    else:
        return r


if __name__ == "__main__":
    topic_name = "stackoverflow_questions"
    endpoint = "https://api.stackexchange.com/2.3/questions"
    todate = int(time.time()) - 18000  # test value: "1619178204"
    fromdate = todate - 100000  # test value: "1617108204"

    response = get_questions(endpoint, fromdate, todate)
    response_json = json.loads(response)
    question_list = response_json["items"]
    log.debug(f"fromdate={fromdate}, todate={todate}, count={len(question_list)}")
    log.debug(question_list)

    # Remove items and print response metadata
    del response_json["items"]
    metadata = response_json
    log.info(f"API metadata: {metadata}")



