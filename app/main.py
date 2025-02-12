from fastapi import FastAPI
from app.api.v1.endpoints import forecast

app = FastAPI()

app.include_router(forecast.router, prefix="/api/v1")