from fastapi import FastAPI
from infra.api.routers import users_routers

app = FastAPI()

app.include_router(users_routers.router)
