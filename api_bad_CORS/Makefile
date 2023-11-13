install_api:
	cd ./api
	python3.11 -m venv venv
	pip install -r requirements.txt


run_api:
	cd ./api
	. ./venv/bin/activate
	uvicorn main:app --reload --port 8000


clean_api:
	cd ./api
	find . -name "*.pyc" -delete
	rm -rf venv
	rm -rf __pycache__ 
