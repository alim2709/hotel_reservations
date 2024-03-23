from fastapi import APIRouter
from app.bookings.dao import BookingDAO
from app.bookings import schemas

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.get("", response_model=list[schemas.SBooking])
async def get_bookings():
    return await BookingDAO.find_all()
