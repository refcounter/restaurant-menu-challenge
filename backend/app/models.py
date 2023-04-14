from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

from .database import Base, engine

class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    icon = Column(String) # path to image on server (to serve as a static asset)
    ingredients = Column(String)
    price = Column(String) # Yeah i know...iam doing this way so i can parseit as decimal later
    count = Column(Integer) # in stock
    meta_data = Column(String) # metadata to feed recomendation engine (and fields i may be forgetting)
    rating = Column(Integer) # user's defined rating
    category = Column(String) # should i extract to another table?
    # season_id = Column(Integer, ForeignKey('season.id'))


class Season(Base):
    __tablename__ = 'seasons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # dishes = relationship('Dish', back_populates=True)

    meta_data = Column(String) # metadata for rec system and fields i may be forgetting

Base.metadata.create_all(engine)
