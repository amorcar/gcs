from typing import List, Optional
from app.models.schemas.base import BaseResponse

class StatusResponse(BaseResponse):
    radio_connected: bool = False
    drone_battery: float
    rssi: Optional[int] = None
    messages: Optional[List[str]] = None
    drone_errors: Optional[List[str]] = None
    server_errors: Optional[List[str]] = None
