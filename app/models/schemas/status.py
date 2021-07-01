from typing import List, Optional
from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: int
    timestamp: int
    radio_connected: bool = False
    drone_battery: float
    rssi: Optional[int] = None
    messages: Optional[List[str]] = None
    drone_errors: Optional[List[str]] = None
    server_errors: Optional[List[str]] = None
