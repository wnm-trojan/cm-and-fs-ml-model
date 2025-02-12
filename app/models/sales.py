from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from app.db.session import Base

class Sales(Base):
    __tablename__ = "sales"
    sale_id = Column(Integer, primary_key=True, index=True)
    crop_id = Column(Integer, ForeignKey("crop_masters.crop_id"))
    sale_qty = Column(Float)
    sale_timestamp = Column(DateTime)