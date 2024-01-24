from pydantic import BaseModel
#test try
#new changes

class BankNotes(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

