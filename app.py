import uvicorn
from fastapi import FastAPI
from BankNotes import BankNotes
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.get("/")
def index():
    return {"message": "Hello, world"}

@app.get("/{name}")
def welcome(name:str):
    return {"message": f"Welcome to Bank Note Authenticator {name}"}

@app.post("/predict")
def predict_bank_notes(data:BankNotes):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if prediction[0] > 0.5:
        prediction = "Fake note"
    else:
        prediction = "Original note"
    return {
        "prediction": prediction
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    

