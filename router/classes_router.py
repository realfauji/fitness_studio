from fastapi import APIRouter, Query
from services.classes_services import get_all_classes


router = APIRouter()

@router.get("/")
def get_classes(timezone: str = Query(default=None, description="User timezone like 'Asia/Kolkata'")):
    return get_all_classes(timezone)
