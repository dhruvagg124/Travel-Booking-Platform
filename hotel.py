from fastapi import FastAPI

app = FastAPI()

@app.get("/hotels")
def hotels():
    return [
        {
            "hotel": "Taj Hotel",
            "city": "Mumbai",
            "price": 7000
        }
    ]
