from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TripRequest(BaseModel):
    destination: str
    days: int
    budget: int

@app.post("/generate-itinerary")
def generate_trip(data: TripRequest):
    return {
        "destination": data.destination,
        "plan": [
            "Day 1: City Tour",
            "Day 2: Beach Visit",
            "Day 3: Shopping"
        ]
    }
