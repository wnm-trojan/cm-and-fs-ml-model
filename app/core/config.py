from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    APP_NAME: str = "CM and FS ML Model"
    DATABASE_URL: str = "mysql+pymysql://wnm:@localhost/fcms_db"
    SECRET_KEY: str = "mysecretkey123"
    ALGORITHM: str = "HS256"

class Config:
    env_file = ".env"

settings = Settings()
load_dotenv()
