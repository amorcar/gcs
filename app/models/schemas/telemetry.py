from typing import List, Optional
from pydantic import BaseModel
from app.models.schemas.base import BaseResponse


class TelemetryData(BaseModel):
    '''Telemetry data retrieved from the GCS
       
       All fields are optional because they may not be
       available in the vehicle.
    '''
    flight_mode: Optional[int]
    voltage: Optional[float]
    battery: Optional[float]
    n_sat: Optional[int]
    gps_fix: Optional[int]
    gps_lat: Optional[float]
    gps_lon: Optional[float] 
    gps_alt: Optional[float]
    yaw: Optional[float]
    pitch: Optional[float]
    roll: Optional[float]
    speed_n: Optional[float]
    speed_e: Optional[float]
    speed_d: Optional[float]
    rc_signal: Optional[float]


class TelemetryResponse(BaseResponse):
    data: Optional[TelemetryData] = None