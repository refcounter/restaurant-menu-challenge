from fastapi import APIRouter, Depends
from typing import List

from .. import database, schemas
from ..repo import menu

router = APIRouter(tags=['Menu'])

@router.get('/')
def main_menu():
    # idk show trending dishes, wheater based recomendations etc
    pass

@router.get('/all', response_model=List[schemas.DishBase])
def get_all(db = Depends(database.get_db)):
    return menu.get_all_dishes()

@router.get('/{id}', response_model=schemas.DishBase)
def get_by_id(db = Depends(database.get_db)):
    return menu.get_by_id(db, id)
