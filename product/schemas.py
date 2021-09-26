from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    amount: int

    class Config:
        orm_mode = True