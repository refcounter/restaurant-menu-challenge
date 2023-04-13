from fastapi_offline import FastAPIOffline as FastAPI # change to fastapi in production

from .database import engine
from . import models
from .routers import menu, payment

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(menu.router)
app.include_router(payment.router)
