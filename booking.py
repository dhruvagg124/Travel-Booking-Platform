from fastapi import FastAPI

app = FastAPI()

@app.post("/book")
def create_booking():
    return {"status": "Booking Confirmed"}
