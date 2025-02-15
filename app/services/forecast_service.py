import pandas as pd
from sqlalchemy.orm import Session
from app.models.sales import Sales
from app.models.crop import Crop
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

def forecast_sales(db: Session, future_periods: int = 12):
    sales_data = db.query(Sales).all()
    crop_names = {crop.crop_id: crop.crop_name for crop in db.query(Crop).all()}
    
    df = pd.DataFrame([(s.crop_id, s.sale_qty, s.sale_timestamp) for s in sales_data],
                      columns=["crop_id", "sale_qty", "sale_timestamp"])
    df["sale_timestamp"] = pd.to_datetime(df["sale_timestamp"])
    df = df.set_index("sale_timestamp")
    
    forecast_results = {}
    
    for crop_id in df["crop_id"].unique():
        crop_df = df[df["crop_id"] == crop_id]["sale_qty"].resample("M").sum()
        
        if len(crop_df) < 3:
            continue  # Skip if there's not enough data
        
        try:
            model = ARIMA(crop_df, order=(3,1,0))  # ARIMA Model (p=3, d=1, q=0)
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=future_periods)
            
            forecast_results[crop_id] = forecast.iloc[-1]  # Forecasted sales for the last period
        except:
            continue  # Skip if the model fails to fit
    
    if not forecast_results:
        return {"top_selling": {}, "low_selling": {}}
    
    sorted_crops = sorted(forecast_results.items(), key=lambda x: x[1], reverse=True)
    
    top_next_month = sorted_crops[0][0] if sorted_crops else None
    low_next_month = sorted_crops[-1][0] if sorted_crops else None
    top_next_year = sorted_crops[0][0] if sorted_crops else None
    low_next_year = sorted_crops[-1][0] if sorted_crops else None
    
    return {
        "top_selling": {
            "next_month": crop_names.get(top_next_month, "Unknown"),
            "next_year": crop_names.get(top_next_year, "Unknown")
        },
        "low_selling": {
            "next_month": crop_names.get(low_next_month, "Unknown"),
            "next_year": crop_names.get(low_next_year, "Unknown")
        }
    }
