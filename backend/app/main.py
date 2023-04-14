from fastapi_offline import FastAPIOffline as FastAPI # change to fastapi in production
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from .database import engine
from .routers import menu, payment, admin, season

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(menu.router)
app.include_router(season.router)
app.include_router(payment.router)


admin_app = Admin(app, engine)
admin_app.add_view(admin.DishView)
admin_app.add_view(admin.SeasonView)


