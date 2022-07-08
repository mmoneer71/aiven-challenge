from time import sleep
from http import HTTPStatus
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from consumer.consume import consume
from consumer.service import get_message_by_id, get_messages_count


def test_produce_consume(producer_client: TestClient):
    old_count = get_messages_count()
    data_json = jsonable_encoder({"message": "hello_kafka!"})
    response = producer_client.post("/send", json=data_json)
    assert response.status_code == HTTPStatus.OK
    sleep(1)
    new_msg = consume(handle_single_message=True)
    assert get_messages_count() == old_count + 1
    assert new_msg.text == "hello_kafka!"
    assert get_message_by_id(new_msg.id)
