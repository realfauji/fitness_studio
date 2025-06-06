from fastapi import HTTPException
from datetime import datetime, timezone
from utils.file_ops import read_json, write_json
from schemas.schemas import BookingRequest, Booking

BOOKINGS_FILE = "data/bookings.json"

def create_booking(booking_req: BookingRequest) -> Booking:
    bookings = read_json(BOOKINGS_FILE)
    new_booking = Booking(
        id = len(bookings) + 1,
        class_id = booking_req.class_id,
        client_name = booking_req.client_name,
        client_email = booking_req.client_email,
        timestamp = datetime.now(timezone.utc)
    )
    bookings.append(new_booking.model_dump())
    write_json(BOOKINGS_FILE, bookings)
    return new_booking

def get_bookings_by_email(email: str):
    bookings = read_json(BOOKINGS_FILE)
    return [client_detail for client_detail in bookings if client_detail["client_email"] == email]

def is_already_booked(email: str, class_id: int) -> bool:
    bookings = read_json(BOOKINGS_FILE)
    return any(client_detail["client_email"] == email and client_detail["class_id"] == class_id for client_detail in bookings)
