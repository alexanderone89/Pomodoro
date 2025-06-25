from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings

# engine = create_engine("sqlite:///pomodoro.sqlite")
# engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5433/pomodoro")
settings = Settings()
engine = create_engine(settings.db_url)

Session = sessionmaker(engine)

def get_db_session()->Session:
    return Session
