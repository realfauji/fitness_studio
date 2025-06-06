from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class FitnessClass(BaseModel):
    id: int
    name: str = Field(..., max_length=200)
    instructor: str
    datetime: datetime
    slots: int

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class Booking(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    timestamp: datetime