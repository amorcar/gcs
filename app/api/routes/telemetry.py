from fastapi import APIRouter

from app.models.schemas.telemetry import TelemetryResponse
from app.services.gcs import get_telemetry

router = APIRouter()

@router.get("", response_model=TelemetryResponse, name="telemetry:get-current-telemetry")
async def retrieve_current_telemetry() -> TelemetryResponse:
    return TelemetryResponse(
        **(await get_telemetry())
    )
