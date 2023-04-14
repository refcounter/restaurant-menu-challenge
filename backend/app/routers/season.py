from fastapi import APIRouter, Depends
from typing import List

from .. import database, schemas
from ..repo import season

router = APIRouter(tags=['Season'], prefix='/season')

@router.get('/all', response_model=List[schemas.SeasonBase])
def get_all(db = Depends(database.get_db)):
    return season.get_all(db, ) # only fetches 5 dishes

@router.get('/{id}', response_model=schemas.SeasonBase)
def get_by_id(db = Depends(database.get_db)):
    return season.get_by_id(db, id)
