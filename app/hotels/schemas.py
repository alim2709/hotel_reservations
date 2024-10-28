from pydantic import BaseModel, ConfigDict

from app.hotels.rooms.models import Rooms


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

    model_config = ConfigDict(from_attributes=True)


class SHotelList(SHotel):
    rooms_left: int
