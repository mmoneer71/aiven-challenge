from producer.const import KAFKA_TOPIC
from producer.kafka_client import client as producer
from producer.models import Message


def get_sample_index() -> Message:
    return Message(message="Nothing to see here :eyes:")


def send_message_to_kafka(new_message: str):
    producer.send(KAFKA_TOPIC, value=bytes(new_message, "utf-8"))
