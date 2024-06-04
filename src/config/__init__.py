import os

from dotenv import load_dotenv

load_dotenv(override=True)


DATA_SET = os.getenv("data_set")

# Confluent-kafka conf
BOOTSTRAP_SERVER = os.getenv("bootstrap_server")
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
SECURITY_PROTOCOL = os.getenv("SECURITY_PROTOCOL")
SSL_MACHENISM = os.getenv("SSL_MACHENISM")
TOPIC_NAME = os.getenv("topic_name")

# Azure Conf
DATASET_URL = os.getenv("dataset_url")
CONNECTION_STRING = os.getenv("connection_string")
FILE_SYSTEM_NAME = os.getenv("file_system_name")
DIRECTORY_NAME = os.getenv("directory_name")
