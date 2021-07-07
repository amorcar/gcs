import logging
from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from app.core.logging import configure_logging

config = Config(".env")

API_PREFIX = "/api"
VERSION = "0.0.0"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
LOG_FILE: str = config("LOG_FILE", default="log/main.log")

PROJECT_NAME: str = config("PROJECT_NAME", default="Ground Crasher Station")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

RADIO_SERIAL_STRING: str = config("RADIO_SERIAL_STRING", default="/dev/ttyUSB0")
# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
configure_logging(log_file=LOG_FILE, log_level=LOGGING_LEVEL)