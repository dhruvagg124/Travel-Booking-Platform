from fastapi import FastAPI

app = FastAPI()

@app.get("/flights")
def flights():
    return [
        {
            "airline": "IndiGo",
            "from": "Delhi",
            "to": "Mumbai",
            "price": 4500
        }
    ]
