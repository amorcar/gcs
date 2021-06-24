from typing import List, Optional
from pydantic import BaseModel


class StatusResponse(BaseModel):
    battery: float
    rssi: Optional[int]
    status: int
    radio_ready: bool = False
    drone_errors: Optional[List[str]]
    server_errors: Optional[List[str]]
