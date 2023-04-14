from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

from .database import Base

class Dish(Base):
    __tablename__ = 'dish'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    icon = Column(String) # path to image on server (to serve as a static asset)
    ingredients = Column(String)
    price = Column(String) # Yeah i know...iam doing this way so i can parseit as decimal later
    count = Column(Integer) # in stock
    meta = Column(String) # metadata to feed recomendation engine (and fields i may be forgetting)
