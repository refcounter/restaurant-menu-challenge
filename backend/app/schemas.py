from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal

class DishBase(BaseModel):
    id: int
    icon: str
    name: str
    ingredients: str
    price: Decimal # see...iam creating a new decimal from String
    count: int
    meta: str
    rating: int
    category: str
    season_id: int

    class Config():
        orm_mode = True

class SeasonBase(BaseModel):
    id: int
    name: str
    dishes: List[DishBase]
    meta: str

    class Config:
        orm_mode = True
