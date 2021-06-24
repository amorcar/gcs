import asyncio
import logging
from app.models.domain.radio import Radio
from app.core.config import RADIO_SERIAL_STRING

radio = None
local_radio_is_ready = False

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
            radio.errors.append('device not found')
            await asyncio.sleep(1)
            continue

def get_radio():
    return radio

def get_telemetry():
    return radio.last_received_telemetry

def get_status():
    return {
        'battery': radio.last_received_telemetry['battery'],
        'rssi': radio.rssi,
        'status': get_status_code(),
        'radio_ready': local_radio_is_ready,
        'drone_errors': get_error_messages(),
        'server_errors': None,
    }

def get_status_code():
    return 0

def get_error_messages():
    if not radio.errors: return None
    n_errors = len(radio.errors)
    return [radio.errors.pop() for _ in range(n_errors)]