from fastapi import APIRouter, HTTPException
from schemas.schemas import BookingRequest
from services.classes_services import reduce_slot, get_all_classes
from services.booking_services import create_booking, get_bookings_by_email, is_already_booked
from services.logger_settings import booking_logger

router = APIRouter()


@router.post("/book")
def book_class(booking: BookingRequest):
    classes = get_all_classes()
    class_obj = next((cls for cls in classes if cls["id"] == booking.class_id), None)

    if not class_obj:
        booking_logger.warning(f"Booking failed - class ID {booking.class_id} not found")
        raise HTTPException(status_code=404, detail="Class not found")
    
    if class_obj["slots"] <= 0:
        booking_logger.warning(f"Booking failed - class {booking.class_id} is full")
        raise HTTPException(status_code=400, detail="Class full")

    if is_already_booked(booking.client_email, booking.class_id):
        booking_logger.warning(f"Booking failed - Duplicate Booking attempt by {booking.client_email} for class {booking.class_id}")
        raise HTTPException(status_code=409, detail="You already booked this class")
    
    reduce_slot(booking.class_id)
    booking_details = create_booking(booking)
    booking_logger.info(f"Booking Successful - {booking.client_email} booked class {booking.class_id}")
    return booking_details


@router.get("/bookings")
def get_bookings(email: str):
    return get_bookings_by_email(email)
