from fastapi import APIRouter
# from fastapi import APIRouter, Body, Depends, HTTPException
# from starlette.status import HTTP_400_BAD_REQUEST

from app.models.schemas.status import StatusResponse
from app.services.gcs import get_status

router = APIRouter()

@router.get("", response_model=StatusResponse, name="status:get-current-status")
async def retrieve_current_status() -> StatusResponse:
    return StatusResponse(
        **get_status()
    )
