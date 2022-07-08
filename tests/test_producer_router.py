"""
This file is mostly for demonstration and data validation.
The actual test of the producer can be found in:
- test_produce_consume.py
"""

from http import HTTPStatus
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient


def test_producer_index(producer_client: TestClient):
    response = producer_client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Nothing to see here :eyes:"}


def test_wrong_input(producer_client: TestClient):
    data_json = jsonable_encoder({"wrong_key": "val"})
    response = producer_client.post("/send", json=data_json)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_long_string(producer_client: TestClient):
    long_str = "x" * 1001
    data_json = jsonable_encoder({"message": long_str})
    response = producer_client.post("/send", json=data_json)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == {"detail": "Message must be 1000 char at most"}
