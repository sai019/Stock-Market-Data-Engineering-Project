import json
from time import sleep

import pandas as pd
from confluent_kafka import Producer

from src.config import BOOTSTRAP_SERVER, DATA_SET, TOPIC_NAME
from src.logger.logger import logging


def delivery_report(err, msg):
    if err is not None:
        logging.error("Delivery failed for User record :  %s", err)
    else:
        logging.info("your message was successfully produced : %s", msg.value())


def get_producer():
    logging.debug("Fetching Kafka producer configuration.")
    conf = {"bootstrap.servers": BOOTSTRAP_SERVER}
    producer = Producer(conf)
    return producer


def main():
    topic_name = TOPIC_NAME
    producer = get_producer()
    df = pd.read_csv(DATA_SET)
    while True:
        dict_stock = df.sample(1).to_dict(orient="records")[0]
        dict_stock_json = json.dumps(dict_stock).encode("utf-8")
        producer.produce(
            topic=topic_name,
            value=dict_stock_json,
            on_delivery=delivery_report,
        )
        sleep(2)
        producer.flush()


if __name__ == "__main__":
    main()
