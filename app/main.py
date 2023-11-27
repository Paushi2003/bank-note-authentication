import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form
from app.BankNotes import BankNotes
import pickle
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict_bank_notes(request: Request, variance: float = Form(...), skewness: float = Form(...), curtosis: float = Form(...), entropy: float = Form(...)):
    data = {
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }

    prediction = classifier.predict([[data['variance'], data['skewness'], data['curtosis'], data['entropy']]])
    if prediction[0] > 0.5:
        prediction = "Fake note"
    else:
        prediction = "Original note"
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction, "data": data})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    

