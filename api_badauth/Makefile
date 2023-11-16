install_api:
	cd ./api && python3 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt && pip install --upgrade pip && pip install --upgrade python-jose


run_api:
	cd ./api && . ./venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 9000

run_frontend:
	docker compose up frontend -d

stop:
	docker compose down

restart_frontend:
	docker compose down frontend && docker compose up frontend -d


clean_api:
	cd ./api && find . -name "*.pyc" -delete && rm -rf venv && rm -rf __pycache__ 
