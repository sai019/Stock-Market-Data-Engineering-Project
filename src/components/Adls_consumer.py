import json

from azure.storage.filedatalake import DataLakeServiceClient
from confluent_kafka import Consumer

from src.config import (
    API_KEY,
    API_SECRET_KEY,
    BOOTSTRAP_SERVER,
    CONNECTION_STRING,
    DIRECTORY_NAME,
    FILE_SYSTEM_NAME,
    SECURITY_PROTOCOL,
    SSL_MACHENISM,
    TOPIC_NAME,
)
from src.exception.exception import CustomException
from src.logger.logger import logging


def get_consumer_config():
    logging.debug("Fetching Kafka consumer configuration.")
    consumer_conf = {
        "sasl.mechanism": SSL_MACHENISM,
        "bootstrap.servers": BOOTSTRAP_SERVER,
        "security.protocol": SECURITY_PROTOCOL,
        "sasl.username": API_KEY,
        "sasl.password": API_SECRET_KEY,
        "group.id": "stockmarket_group",
        "auto.offset.reset": "latest",
    }
    return consumer_conf


def upload_to_adls(file_system_client, DIRECTORY_NAME, file_name, data):
    directory_client = file_system_client.get_directory_client(directory=DIRECTORY_NAME)
    file_client = directory_client.create_file(file_name)
    file_client.append_data(data, 0, len(data))
    file_client.flush_data(len(data))
    logging.info(f"Uploaded message to {DIRECTORY_NAME} folder")


def main():
    logging.info("Starting the Kafka consumer.")
    topic_name = TOPIC_NAME
    consumer = Consumer(get_consumer_config())
    consumer.subscribe([topic_name])
    logging.info(f"Subscribed to Kafka topic: {topic_name}")
    connection_string = CONNECTION_STRING

    # Create a DataLakeServiceClient
    datalake_service_client = DataLakeServiceClient.from_connection_string(connection_string)
    logging.info("Connected to Azure Data Lake Storage.")

    # Get the FileSystemClient
    file_system_client = datalake_service_client.get_file_system_client(file_system=FILE_SYSTEM_NAME)
    logging.info(f"Accessed file system: {FILE_SYSTEM_NAME}")

    count = 0
    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            message = msg.value().decode("utf-8")
            message_dict = json.loads(message)
            file_name = f"stock_market_{count}.json"
            data = json.dumps(message_dict)
            logging.info(f"Uploading data to ADLS: Directory: {DIRECTORY_NAME}, File: {file_name}")
            upload_to_adls(file_system_client, DIRECTORY_NAME, file_name, data)
            count += 1
            logging.info(f"Processed message {count}.")
        except CustomException as e:
            logging.error(f"Error processing message {count}: {str(e)}")


if __name__ == "__main__":
    main()
