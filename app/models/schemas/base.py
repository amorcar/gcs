from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: int
    system_timestamp: int