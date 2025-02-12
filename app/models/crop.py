from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Crop(Base):
    __tablename__ = "crop_masters"
    crop_id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String(255), index=True)