from consumer.const import (
    CLIENT_ID,
    GROUP_ID,
    KAFKA_TOPIC,
    OFFSET_RESET,
    SASL_MECHANISM,
    SEC_PROTOCOL,
)
from kafka import KafkaConsumer
from consumer.settings import (
    CA_CERT_PATH,
    KAFKA_HOST,
    KAFKA_PASSWORD,
    KAFKA_USERNAME,
    SASL_PORT,
)

# Loosely based on: https://help.aiven.io/en/articles/5343895-python-examples-for-testing-aiven-for-apache-kafka
# and https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

client = KafkaConsumer(
    KAFKA_TOPIC,
    auto_offset_reset=OFFSET_RESET,
    bootstrap_servers="{}:{}".format(KAFKA_HOST, SASL_PORT),
    client_id=CLIENT_ID,
    group_id=GROUP_ID,
    sasl_mechanism=SASL_MECHANISM,
    sasl_plain_username=KAFKA_USERNAME,
    sasl_plain_password=KAFKA_PASSWORD,
    security_protocol=SEC_PROTOCOL,
    ssl_cafile=CA_CERT_PATH,
)
