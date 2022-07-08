import pytest
from fastapi.testclient import TestClient

from producer.networking import app


@pytest.fixture
def producer_client() -> TestClient:
    return TestClient(app)
