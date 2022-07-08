from fastapi import APIRouter, HTTPException

from producer.models import Message
from producer.samples import sample_index_message
from producer.service import get_sample_index, send_message_to_kafka

producer_api = APIRouter()


@producer_api.get(
    "/",
    tags=["Index"],
    responses={
        200: {
            "model": Message,
            "description": "So, it works!",
            "content": {"application/json": {"example": sample_index_message}},
        }
    },
)
async def index() -> Message:
    return get_sample_index()


@producer_api.post(
    "/send",
    tags=["Producer"],
    responses={
        200: {
            "model": str,
            "description": "Message sent to Kafka",
            "content": {
                "application/json": {"example": "Message ping sent successfully"}
            },
        }
    },
)
async def send_message(new_message: Message) -> str:
    if len(new_message.message) > 1000:
        raise HTTPException(status_code=422, detail="Message must be 1000 char at most")
    send_message_to_kafka(new_message.message)
    return f"Message {new_message.message} sent succesfully"
