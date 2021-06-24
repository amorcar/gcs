from fastapi import APIRouter
from starlette.responses import RedirectResponse
from app.api.routes import status

router = APIRouter()

@router.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")

router.include_router(status.router, tags=["status"], prefix="/status")