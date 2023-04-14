from sqladmin import ModelView
from .. import models

class DishView(ModelView, model=models.Dish):
    column_list = ['id', 'name', 'category']
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

class SeasonView(ModelView, model=models.Season):
    column_list = ['id', 'name', ]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True   
