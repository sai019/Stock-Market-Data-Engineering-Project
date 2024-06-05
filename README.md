<h1 align="center">Stock Market Real-Time Data Pipeline (Kafka)</h1>

## Introduction :<br>
This project guides you through building a real-time data pipeline for stock market data using Kafka.

## 📐 Architecture :<br>
<img align="center" alt="" src="https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Images/Project%20Architecture.gif" />

## 🛠️ Tech Stack Used :<br>
  - Programming Language - Python
  - Sql
  - Confluent Kafka
  - Azure
    -  ADLS (Azure data lake gen2)
    -  Azure Synapse Analytics
    - Serverless Sql pool
  
## 📈 Dataset Used :<br>
Here is the Mock dataset used in the project - [Mock Data](https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Data/indexProcessed.csv)

## 📁 Cloning this project :<br> 
```
git clone https://github.com/sai019/Stock-Market-Data-Engineering-Project.git
```
Navigate to the Project Directory :

```
cd Stock-Market-Data-Engineering-Project  # Replace with the actual folder name
```
Create and Activate a Virtual Environment :
```
conda create -p venv python=3.9 -y
```
You can Replace ```venv``` with a desired name for your virtual environment.
```
conda activate venv/
```
Install Project Dependencies :
```
pip install -r requirements.txt
```
All set now you cloned this project successfully.

## 🚀 Project Work Flow :<br>
- Confluent Kafka setup :
  - Click on the links below to follow the steps : 
    1. [Set up the Confluent Kafka cluster.](https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Docs/ConfluentClusterSetup.md)
    2. [Create a topic in Confluent Kafka.](https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Docs/Confluent%20Topic%20Creation.md)
    3. [Create Kafka cluster API keys and secrets.](https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Docs/Kafka%20key%20and%20secrets.md)
    4. [How to create .env file.](https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Docs/env_doc.md)
- Create Azure Data Lake Gen2 and Azure Synapse Analytics services in the Azure portal.
- Execute ```src/components/producer_stream.py``` to generate messages for the Kafka topic.
- This is what a message produced to a Confluent Kafka topic looks like on the confluent dashboard. The image shows the message details, including timestamp, offset, 
    partition, key, and value.
 
  - <img align="center" alt="" src="https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Images/Message_details.png" height="400"/>
- Run ```src/components/Adls_consumer.py``` to consume messages from the Kafka topic and upload them to Azure Data Lake Gen2 as JSON data.
- Using Azure Data Lake and the serverless SQL pool in Azure Synapse Analytics, you can execute SQL queries on the JSON data stored in Azure Data Lake to gain insights.

## 🌐 Sources and Links :<br>
  - https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-directory-file-acl-python?tabs=azure-ad
  - https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/query-json-files
  - https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html
