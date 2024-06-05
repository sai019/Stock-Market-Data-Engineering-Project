# How to Create the .env File in the Project Root Directory

To configure your project, you need to create a `.env` file in the root directory of your project. This file will store various environment variables required for Kafka and Azure configurations. Follow the steps below:

1. Open your project root directory.
2. Create a new file named `.env`.

3. Open the `.env` file and add the following content, filling in the appropriate values for each variable:

```env
# Data Set
data_set = my_data_set # The path of the source data set


# Kafka Configuration
bootstrap_server = my_bootstrap_server # Your Kafka bootstrap server address
API_KEY = my_api_key # Your Kafka API key for authentication
API_SECRET_KEY = my_api_secret_key # Your Kafka API secret key for authentication

# No need to change the values to this
SECURITY_PROTOCOL = 'SASL_SSL'  # Security protocol for Kafka
SSL_MECHANISM = 'PLAIN'  # SSL mechanism for authentication

topic_name = my_topic_name # Your Kafka topic name for message publishing


# Azure Configuration
connection_string = my_connection_string # Your Azure Storage Account Connection String
file_system_name = my_file_system_name # Your Azure Data lake Storage file system name
directory_name = my_directory_name # Your directory name within the Azure Data lake Storage file system
