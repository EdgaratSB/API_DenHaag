from fastapi import FastAPI
import models.models as models
import database.database as database
from database.database import engine
from routers import cases, roles, access_levels


app = FastAPI(debug=True)

models.Base.metadata.create_all(bind=engine)

app.include_router(roles.router)
app.include_router(cases.router)
app.include_router(access_levels.router)