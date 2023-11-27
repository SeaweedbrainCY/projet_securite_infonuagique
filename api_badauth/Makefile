install_api:
	cd ./api && python3 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt && pip install --upgrade pip && pip install --upgrade python-jose


run_api:
	cd ./api && . ./venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 9000

clean_api:
	cd ./api && find . -name "*.pyc" -delete && rm -rf venv && rm -rf __pycache__


install_api_secure:
	cd ./api_secure && python3 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt && pip install --upgrade pip && pip install --upgrade python-jose


run_api_secure:
	cd ./api_secure && . ./venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 9000

clean_api_secure:
	cd ./api_secure && find . -name "*.pyc" -delete && rm -rf venv && rm -rf __pycache__

run_frontend:
	docker compose -f docker-compose-local.yml up frontend -d

stop:
	docker compose -f docker-compose-local.yml down

restart_frontend:
	docker compose -f docker-compose-local.yml down frontend && docker compose -f docker-compose-local.yml up frontend -d
