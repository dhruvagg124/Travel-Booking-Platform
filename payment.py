from fastapi import FastAPI

app = FastAPI()

@app.post("/pay")
def payment():
    return {"status": "Payment Successful"}
