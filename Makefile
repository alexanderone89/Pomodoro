.DEFAULT_GOAL := help

HOST ?= 0.0.0.0
PORT ?= 8000

## Run the application using uvicorn with provided arguments or defaults
run:
# 	poetry run gunicorn main:app -c gunicorn.conf.py
	poetry run uvicorn app.main:app --host $(HOST) --port $(PORT) --reload
#     poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file $(ENV_FILE)

install: ## Install a dependency using poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Uninstall a dependency using poetry
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply:
	alembic upgrade head

help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'