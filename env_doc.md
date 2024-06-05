# How to Create the .env File in the Project Root Directory

To configure your project, you need to create a `.env` file in the root directory of your project. This file will store various environment variables required for Kafka and Azure configurations. Follow the steps below:

1. Open your project root directory.
2. Create a new file named `.env`.

3. Open the `.env` file and add the following content, filling in the appropriate values for each variable:

```env
# Data Set
data_set=my_data_set

# Kafka Configuration
bootstrap_server=my_bootstrap_server
API_KEY=my_api_key
API_SECRET_KEY=my_api_secret_key
SECURITY_PROTOCOL=SSL
SSL_MECHANISM=PLAIN
topic_name=my_topic_name

# Azure Configuration
connection_string=my_connection_string
file_system_name=my_file_system_name
directory_name=my_directory_name
