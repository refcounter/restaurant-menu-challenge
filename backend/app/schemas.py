from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal
from typing_extensions import TypedDict

class Storage(TypedDict):
    _path: str

class ImageField(BaseModel):
    _name: str
    _storage: Storage

class DishBase(BaseModel):
    id: int
    icon: object
    name: str
    ingredients: str
    price: Decimal # see...iam creating a new decimal from String
    count: int
    rating: int
    category: str
    season_id: int

    class Config():
        orm_mode = True
        arbitrary_types_allowed = True
        

class SeasonBase(BaseModel):
    id: int
    name: str
    dishes: List[DishBase]

    class Config:
        orm_mode = True
