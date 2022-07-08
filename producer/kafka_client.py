from kafka import KafkaProducer

from producer.const import SASL_MECHANISM, SEC_PROTOCOL
from producer.settings import (
    CA_CERT_PATH,
    KAFKA_HOST,
    KAFKA_PASSWORD,
    KAFKA_USERNAME,
    SASL_PORT,
)

# Loosely based on: https://help.aiven.io/en/articles/5343895-python-examples-for-testing-aiven-for-apache-kafka
# and https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

client = KafkaProducer(
    bootstrap_servers=f"{KAFKA_HOST}:{SASL_PORT}",
    sasl_mechanism=SASL_MECHANISM,
    sasl_plain_password=KAFKA_PASSWORD,
    sasl_plain_username=KAFKA_USERNAME,
    security_protocol=SEC_PROTOCOL,
    ssl_cafile=CA_CERT_PATH,
)
