from datetime import date
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.bookings.models import Bookings
from app.dao.base import BaseDao
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class HotelsDAO(BaseDao):
    model = Hotels

    @classmethod
    async def find_all(
        cls, date_from: date, date_to: date, location: Optional[str] = None
    ):
        async with async_session_maker() as session:
            # query = select(cls.model)
            #
            # result = await session.execute(query)
            #
            # return result.scalars().all()

            query = (
                select(cls.model)
                .join(Rooms)
                .join(Bookings)
                .filter(Rooms.hotel_id == cls.model.id)
                .filter(Bookings.room_id == Rooms.id)
                .filter(date_from < Bookings.date_to)
                .filter(date_to > Bookings.date_from)
                .options(selectinload(cls.model.rooms).selectinload(Rooms.bookings))
                .distinct()  # Ensure each hotel appears only once in the result
            )
            result = await session.execute(query)
            available_hotels = result.scalars().all()

            return available_hotels
