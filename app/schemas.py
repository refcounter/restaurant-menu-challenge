from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class DishBase(BaseModel):
    id: int
    icon: str
    name: str
    ingredients: str
    price: Decimal # see...iam creating a new decimal from String
    count: int
    meta: str

    class Config():
        orm_mode = True
