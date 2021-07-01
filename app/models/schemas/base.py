from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: int
    timestamp: int