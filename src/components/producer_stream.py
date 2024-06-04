import json
from time import sleep

import pandas as pd
from confluent_kafka import Producer

from src.config import (
    API_KEY,
    API_SECRET_KEY,
    BOOTSTRAP_SERVER,
    DATA_SET,
    SECURITY_PROTOCOL,
    SSL_MACHENISM,
    TOPIC_NAME,
)
from src.exception.exception import CustomException
from src.logger.logger import logging


def delivery_report(err, msg):
    if err is not None:
        logging.error("Delivery failed for User record :  %s", err)
    else:
        logging.info("your message was successfully produced : %s", msg.value())


def get_producer():
    logging.info("Fetching Kafka producer configuration.")
    conf = {
        "sasl.mechanism": SSL_MACHENISM,
        "bootstrap.servers": BOOTSTRAP_SERVER,
        "security.protocol": SECURITY_PROTOCOL,
        "sasl.username": API_KEY,
        "sasl.password": API_SECRET_KEY,
    }
    producer = Producer(conf)
    return producer


def main():
    topic_name = TOPIC_NAME
    producer = get_producer()
    df = pd.read_csv(DATA_SET)
    while True:
        try:
            dict_stock = df.sample(1).to_dict(orient="records")[0]
            dict_stock_json = json.dumps(dict_stock).encode("utf-8")
            logging.info(f"Sending message to Kafka topic: {topic_name}")
            producer.produce(
                topic=topic_name,
                value=dict_stock_json,
                on_delivery=delivery_report,
            )
            sleep(2)
            producer.flush()
        except CustomException as e:
            logging.error(f"Error producing message: {e}")


if __name__ == "__main__":
    main()
