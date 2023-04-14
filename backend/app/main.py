from fastapi_offline import FastAPIOffline as FastAPI # change to fastapi in production
from sqladmin import Admin

from .database import engine
from .routers import menu, payment, admin

app = FastAPI()
app.include_router(menu.router)
app.include_router(payment.router)

admin_app = Admin(app, engine)
admin_app.add_view(admin.DishView)
admin_app.add_view(admin.SeasonView)


