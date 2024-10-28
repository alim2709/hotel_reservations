from datetime import date

from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.bookings import schemas
from app.bookings.schemas import SBooking
from app.exceptions import RoomFullyBooked
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.get("", response_model=list[schemas.SBooking])
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:

    return await BookingDAO.find_all()


@router.post("", response_model=schemas.SBooking)
async def add_booking(
    booking: schemas.SNewBooking,
    user: Users = Depends(get_current_user),
):

    bookings = await BookingDAO.add(
        user.id, booking.room_id, booking.date_from, booking.date_to
    )
    if not bookings:
        raise RoomFullyBooked
    return bookings
