from fastapi import FastAPI
from app.users.models import Users
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.bookings.routers import router as booking_router
from app.users.routers import router as users_router
from app.hotels.routers import router as hotels_router

app = FastAPI()

app.include_router(users_router)
app.include_router(booking_router)
app.include_router(hotels_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
