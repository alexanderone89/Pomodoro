.DEFAULT_GOAL := help

HOST ?= 0.0.0.0
PORT ?= 8000

run:
    uvicorn main:app --host $(HOST) --port $(PORT)