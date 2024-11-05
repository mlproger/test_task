from fastapi import APIRouter
from .veiw import router as greeting_router

router = APIRouter()
router.include_router(router=greeting_router, prefix="/api")