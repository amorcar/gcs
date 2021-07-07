from typing import Callable

from fastapi import FastAPI
from app.models.domain.radio import Radio
from app.services.gcs import initialize_radio, connect_radio_in_background

def create_start_app_handler(app: FastAPI) -> Callable:  # typinitialize_radio, e: ignore
    async def start_app()  -> None:
        initialize_radio()
        # Connect to local radio
        connect_radio_in_background()
    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def stop_app() -> None:
        # Disconnect and stop radio
        pass

    return stop_app