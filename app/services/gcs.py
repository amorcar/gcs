import asyncio
import logging
from datetime import datetime
from app.models.domain.radio import Radio
from app.core.config import RADIO_SERIAL_STRING

radio = None
local_radio_is_connected = False
messages = []
server_errors = []

def get_base_response():
    return {
        'status': get_status_code(),
        'timestamp': datetime.now().timestamp(),
    }

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
            global local_radio_is_ready
            local_radio_is_ready = True
            break
        except BaseException as e:
            # radio.errors.append('device not found')
            await asyncio.sleep(1)
            continue

def get_status_code():
    return 0

def get_messages():
    if not messages: return None
    return (messages.pop() for _ in messages)

def get_error_messages():
    if not radio.errors: return None
    return (radio.errors.pop() for _ in radio.errors)

def get_server_errors():
    if not radio.errors: return None
    return (server_errors.pop() for _ in server_errors)

async def get_status():
    return dict(
        get_base_response(),
        **{
            'radio_connected': local_radio_is_connected,
            'drone_battery': radio.last_received_telemetry['battery'],
            'rssi': radio.rssi,
            'messages': get_messages(),
            'drone_errors': get_error_messages(),
            'server_errors': None,
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