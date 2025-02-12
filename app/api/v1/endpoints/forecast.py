from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.forecast_service import forecast_sales

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/forecast/")
def get_forecast(db: Session = Depends(get_db)):
    forecast_data = forecast_sales(db, future_periods=12)
    return forecast_data