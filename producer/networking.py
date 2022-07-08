from fastapi import FastAPI

from producer import __version__
from producer.router import producer_api

app = FastAPI(
    version=__version__,
    title="Producer API",
    description="Producer app API for Aiven challenge",
)

app.include_router(producer_api)
