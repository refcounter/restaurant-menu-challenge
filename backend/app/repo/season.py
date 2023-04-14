from fastapi import HTTPException

from sqlalchemy.orm import Session

from .. import models

def get_all(db: Session):
    return db.query(models.Season).all()

def get_by_id(db: Session, id: int):
    season = db.get(models.Season, id)
    
    if not season:
        raise HTTPException(status_code=404, detail='season not found')
    return season
