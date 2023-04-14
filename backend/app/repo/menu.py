from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import models

def get_all_dishes(db: Session):
    return db.query(models.Dish).all()

def get_by_id(db: Session, id: int):
    dish = db.query(models.Dish).get(id)

    if not dish:
        raise HTTPException(status_code=404, detail='not found')

    return dish
