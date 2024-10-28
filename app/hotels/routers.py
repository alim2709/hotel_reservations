from typing import Optional

from fastapi import APIRouter

from app.hotels import schemas
from app.hotels.dao import HotelsDAO

router = APIRouter(prefix="/hotels", tags=["hotels"])


@router.get("", response_model=list[schemas.SHotel])
async def get_all_hotels(location, date_from, date_to):
    result = await HotelsDAO.find_all(date_from=date_from, date_to=date_to)
    print(result)
    if result is None:
        return {"message": "No hotels found"}
    return result
