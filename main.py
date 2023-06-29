import model
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
model = model.make_model()

@app.get("/aktualna-data")
def get_aktualna_data():
    aktualna_data = datetime.now()
    return {"aktualna_data": aktualna_data}

@app.post("/predict")
def predict_price(data):
    value = model.predict([[
        data.kolumna1,
        data.kolumna2,
        data.kolumna3,
    ]])
    return value[0]