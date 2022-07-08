import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

KAFKA_HOST = os.getenv("KAFKA_HOST", "kafka-278eafb1-aiven-challenge.aivencloud.com")
SASL_PORT = os.getenv("SASL_PORT", 22523)
KAFKA_USERNAME = os.getenv("KAFKA_USERNAME", "")
KAFKA_PASSWORD = os.getenv("KAFKA_PASSWORD", "")
CA_CERT_PATH = os.getenv("CA_CERT_PATH", "ca.pem")
