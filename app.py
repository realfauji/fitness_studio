from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from router.booking_router import router as BookingRouter
from router.classes_router import router as ClassesRouter

app = FastAPI()


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


app.include_router(BookingRouter, tags=["Bookings"], include_in_schema=True)
app.include_router(ClassesRouter, prefix="/classes", tags=["Classes"], include_in_schema=True)