import logging
class Radio:
    '''Mock radio'''
    def __init__(self, id=0):
        logging.debug('Initializing RADIO')
        self.connection_tries = 0
        self.last_received_telemetry = {
            'flight_mode': 1,
            'voltage': 14.2,
            'battery': 0.75,
            'n_sat': 8,
            'gps_fix': 2,
            'gps_lat': 28.071637,
            'gps_lon': -15.457188,
            'gps_alt': 23.1,
            'yaw': 123.39,
            'pitch': 4.32,
            'roll': 2.97,
            'speed_n': 20.29,
            'speed_e': 3.51,
            'speed_d': 0.23,
            'rc_signal': 0.3,
        }
        self.errors = []
        self.rssi = 123

    async def connect_to_serial(self, *args, **kwargs):
        if self.connection_tries < 5:
            self.connection_tries += 1
            raise BaseException('Device not found')
    
    def send_rtl(self):
        print("Sending RTl")
    
    def send_start_mission(self):
        print("Sending start mission")