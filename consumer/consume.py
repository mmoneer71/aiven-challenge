from consumer.kafka_client import client
from consumer.service import create_message, get_messages_count


def _handle_message(message):
    text = message.value.decode("utf-8")
    print(f"Message received: {text}")
    return create_message(text)


def consume(handle_single_message: bool = False):
    print("Initializing consumer app")
    for message in client:
        result = _handle_message(message)
        if handle_single_message:
            return result
        if result:
            print(f"New message created in db with id: {result.id}")
            print(f"Total number of messages: {get_messages_count()}")


if __name__ == "__main__":
    consume()
