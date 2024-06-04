<h1 align="center">Stock Market Real-Time Data Pipeline (Kafka)</h1>

## Introduction :<br>
This project guides you through building a real-time data pipeline for stock market data using Kafka.

## Architecture :<br>
<img align="center" alt="" src="https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Images/Project%20Architecture.gif" />

## Technology Used :<br>
  - Programming Language - Python
  - Sql
  - Confluent Kafka
  - Azure
    -  ADLS (Azure data lake gen2)
    -  Azure Synapse Analytics
    - Serverless Sql pool
  
## Dataset Used :<br>
Here is the Mock dataset used in the project - [Mock Data](https://github.com/sai019/Stock-Market-Data-Engineering-Project/blob/main/Data/indexProcessed.csv)

## Cloning this project :<br> 
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

## Project Work Flow:<br>
1. setup the confluent kafka cluster on the 




