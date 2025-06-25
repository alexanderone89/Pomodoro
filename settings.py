from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_TOKEN_ID: str = "<DEFAULT_TOKEN_ID>"
    sqlite_db_name: str = "pomodoro.sqlite"