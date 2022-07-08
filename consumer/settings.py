import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

KAFKA_HOST = os.getenv("KAFKA_HOST", "kafka-278eafb1-aiven-challenge.aivencloud.com")
SASL_PORT = os.getenv("SASL_PORT", 22523)
KAFKA_USERNAME = os.getenv("KAFKA_USERNAME", "")
KAFKA_PASSWORD = os.getenv("KAFKA_PASSWORD", "")
CA_CERT_PATH = os.getenv("CA_CERT_PATH", "ca.pem")


PSQL_HOST = os.getenv("PSQL_HOST", "pg-2ca88aa3-aiven-challenge.aivencloud.com")
PSQL_PORT = os.getenv("PSQL_PORT", 22510)
PSQL_NAME = os.getenv("PSQL_NAME", "assignment")
PSQL_USERNAME = os.getenv("PSQL_USERNAME", "avnadmin")
PSQL_PASSWORD = os.getenv("PSQL_PASSWORD", "")
