from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # sqlite_db_name: str = "pomodoro.sqlite"
    DB_HOST: str = "localhost"
    DB_PORT: int = "5433"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    # DB_DRIVER: str = "postgresql+psycopg2"
    # асинхронный драйвер postgresql
    DB_DRIVER: str = "postgresql+asyncpg"
    DB_NAME: str = "pomodoro"

    CACHE_HOST: str = "localhost"
    CACHE_PORT: int = 6379
    CACHE_DB: int = 0

    JWT_SECRET_KEY: str = "secret_key"
    JWT_ENCODE_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_DAY: int = 7


    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_SECRET_KEY: str = ""
    GOOGLE_REDIRECT_URI: str = ""
    GOOGLE_TOKEN_URL: str = "https://accounts.google.com/o/oauth2/token"

    YANDEX_CLIENT_ID: str = ""
    YANDEX_SECRET_KEY: str = ""
    YANDEX_REDIRECT_URI: str = ""
    YANDEX_TOKEN_URL: str = "https://oauth.yandex.ru/token"

    CELERY_REDIS_URL: str = "redis://localhost:6379"
    from_email: str="alexanderone89@mail.ru"
    SMTP_HOST: str = "smtp.mail.ru"
    SMTP_PORT: int = 465
    SMTP_PASSWORD: str = "3ir3SvZowRbQg8zdBC3V"

    @property
    def db_url(self):
        # print(f'[DB URL]             {self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def google_redirect_url(self)->str:
        return f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"

    @property
    def yandex_redirect_url(self)->str:
        return f"https://oauth.yandex.ru/authorize?response_type=code&client_id={self.YANDEX_CLIENT_ID}&redirect_uri={self.YANDEX_REDIRECT_URI}"