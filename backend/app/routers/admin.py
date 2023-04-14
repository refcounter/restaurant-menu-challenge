from sqladmin import ModelView
from .. import models

class DishView(ModelView, model=models.Dish):
    column_list = ['id', 'name', 'category']
    form_include_pk = True

    
class SeasonView(ModelView, model=models.Season):
    column_list = ['id', 'name', ]
