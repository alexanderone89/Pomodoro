import multiprocessing
import os

from dotenv import load_dotenv
from uvicorn.workers import UvicornWorker

bind = "0.0.0.0:8000"
workers = 4
# workers = 4 # multiprocessing.cpu_count() * 2 + 1
worker_class = UvicornWorker #"uvicorn.workers.UvicornWorker"

environment = os.getenv("ENV")

env = os.path.join(os.getcwd(), f".{environment}.env")
if os.path.exists(env):
    load_dotenv(env)

# print(os.getenv("YANDEX_CLIENT_ID"))