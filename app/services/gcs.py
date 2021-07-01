import asyncio
import logging
from datetime import datetime
from enum import Enum
from app.models.domain.radio import Radio
from app.core.config import RADIO_SERIAL_STRING
from app.resources.strings import (
    LOCAL_RADIO_DEVICE_FOUND,
    LOCAL_RADIO_DEVICE_NOT_FOUND,
)
from app.resources.error_codes import (
    DEVICE_NOT_FOUND,
)

radio = None
local_radio_is_connected = False
messages = []
server_errors = []

class STATUS(Enum):
    OK = 0
    WARNING = 1
    ERROR = 2
current_status: STATUS = 0

def get_status_code():
    return current_status

def set_status(new_status: STATUS):
    global current_status
    current_status = new_status

def get_base_response():
    return {
        'status': get_status_code(),
        'timestamp': datetime.now().timestamp(),
    }

def add_server_error(code: int, message: str):
    server_errors.append({
        'id': code,
        'message': message,
    })

def remove_server_errors_with_code(code:int):
    global server_errors
    filtered_messages = list(
        filter(lambda m: m['id'] != code, server_errors)
    )
    server_errors = filtered_messages

def get_radio():
    return radio

def initialize_radio():
    global radio
    radio = Radio()

def connect_radio_in_background():
    logging.debug('creating local connection task')
    asyncio.create_task(try_radio_connection())
    logging.debug('local connection task created')

async def try_radio_connection():
    while True:
        try:
            await radio.connect_to_serial(RADIO_SERIAL_STRING)
            logging.info('radio connected')
            global local_radio_is_connected
            local_radio_is_connected = True
            messages.append(LOCAL_RADIO_DEVICE_FOUND)
            remove_server_errors_with_code(DEVICE_NOT_FOUND)
            break
        except BaseException as e:
            add_server_error(DEVICE_NOT_FOUND, LOCAL_RADIO_DEVICE_NOT_FOUND)
            await asyncio.sleep(1)
            continue

def get_messages():
    if not messages: return None
    return (messages.pop() for _ in messages)

def get_radio_errors():
    if not radio.errors: return None
    return (radio.errors.pop() for _ in radio.errors)

def get_server_errors():
    if not server_errors: return None
    return (server_errors.pop()['message'] for _ in server_errors)

async def get_status():
    return dict(
        get_base_response(),
        **{
            'radio_connected': local_radio_is_connected,
            'drone_battery': radio.last_received_telemetry['battery'],
            'rssi': radio.rssi,
            'messages': get_messages(),
            'drone_errors': get_radio_errors(),
            'server_errors': get_server_errors(),
        }
    )

async def get_telemetry():
    return dict(
        get_base_response(),
        **{
            'data': get_telemetry_data()
        }
    )

def get_telemetry_data():
    return radio.last_received_telemetry