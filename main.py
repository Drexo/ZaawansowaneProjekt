from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/aktualna-data")
def get_aktualna_data():
    aktualna_data = datetime.now()
    return {"aktualna_data": aktualna_data}