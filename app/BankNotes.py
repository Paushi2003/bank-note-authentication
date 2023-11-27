from pydantic import BaseModel

class BankNotes(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

