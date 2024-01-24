from pydantic import BaseModel
#test try
class BankNotes(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

