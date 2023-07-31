# Aiven Challenge

## Overview
Simple demo producer/consumer application using Python and Kafka. The producer accepts data through a REST API and publishes to the Kafka queue, the consumer then consumes the data from the queue and logs it into a PostgreSQL database.

Tech Stack: Python, FastAPI, PostgreSQL, SQLAlchemy, Kafka, Aiven tools for hosting

## Running instructions

The solution has been written and tested with Python version 3.8.10.

If you want to setup the virtual environment first, please make sure python3.8-venv is installed or install it by running:

`sudo apt install python3.8-venv`

then run:

`python3 -m venv .venv`

and activate the virtual env:

`source .venv/bin/activate`

  
To setup the solution, please install the dependencies by running: `pip install -r requirements.txt`, preferably inside a virtual env to avoid conflicts.

  
Also the project uses `python-dotenv`, so it loads environment variables into a Python session by using a `.env` file. A sample can be found in `.env.example`, please create a new `.env` file and copy the values into it. Since you might not have access to the services I created in the Aiven console, you can find the values I used here:

  

```
KAFKA_HOST=kafka-278eafb1-aiven-challenge.aivencloud.com
SASL_PORT=22523
KAFKA_USERNAME=avnadmin
KAFKA_PASSWORD=CEFMBGv1hBYryHsX
CA_CERT_PATH=ca.pem
PSQL_HOST=pg-2ca88aa3-aiven-challenge.aivencloud.com
PSQL_PORT=22510
PSQL_NAME=assignment
PSQL_USERNAME=avnadmin
PSQL_PASSWORD=glMiRwgwT7Fjj43m
```

Understandably, these values (especially the sensitive ones) would not be shared as plain text or even in the repo at all, but I shared here for the sake of the assignment only.

You can use the script `producer_start.sh` to run the producer from the terminal, which will start the API on `localhost:8000`. The API docs are available at the endpoint `/docs`, which can also be used to send requests to the API and also shows a sample curl request.


In a separate terminal, you can use the script `consumer_start.sh` to run the consumer from the terminal (please activate the virtualenv first), which will run a generic python script and print output to the terminal. Please run `export PYTHONPATH=.` if you face any import issues (not ideal, but works for now) and make sure both producer and consumer apps are running if you want to demo the full project.


Tests can be also run by using the following command:

`python -m pytest tests/`

Please make sure there are no queued messages before running the tests to avoid issues, you can do that by running the consumer until no further messages appear.

  
After setting up the project and running both components, you can send a POST request to the producer which will send a single message to Kafka (more details in the Swagger docs). The consumer will then pick the message up and add it to the database.


## Setting up the database

These steps are already done, and only written here for clarification:

First, the database `assignment` was created through the Aiven PostgreSQL console.
Second, the alembic migrations are run as follows: `alembic upgrade head` which will create the tables as per the spec in `db_models.py` and the migrations revision.


## Discussion

Normally, the tests would run in a separate env/database, however, for the sake of the assignment/demo only they are running on the same database.

Also, the producer and consumer apps are considered two standalone apps in theory, however, to avoid redundancy they are sharing the same `.env` file.

The producer app did not need to be an API in particular, but I only did it to make the producer and consumer apps different and showcase more work! :D
