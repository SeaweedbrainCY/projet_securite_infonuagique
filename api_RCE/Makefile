install_api:
	cd ./api && python3.11 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt


run_api:
	cd ./api && . ./venv/bin/activate && uvicorn main:app --reload --port 8000

clean_api:
	cd ./api && find . -name "*.pyc" -delete && rm -rf venv && rm -rf __pycache__ && rm -R media

install_api_secure:
	cd ./api_safe && python3.11 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt


run_api_secure:
	cd ./api_safe && . ./venv/bin/activate && uvicorn main:app --reload --port 8000

clean_api_secure:
	cd ./api_safe && find . -name "*.pyc" -delete && rm -rf venv && rm -rf __pycache__ && rm -R media


run_frontend:
	docker compose up frontend -d

stop:
	docker compose down

restart_frontend:
	docker compose down frontend && docker compose up frontend -d