import redis
from settings import Settings


def get_redis_connection()->redis.Redis:
    settings = Settings()
    return redis.Redis(host=settings.CACHE_HOST,
                       port=settings.CACHE_PORT,
                       db=settings.CACHE_DB)

def set_pomodoro_count():
    redis_connection = get_redis_connection()
    redis_connection.json('pomodoro_count', 2)
