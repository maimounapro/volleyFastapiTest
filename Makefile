run:
	uvicorn main:app --reload --port 8000
lib:
	pip3 freeze > requirements.txt
build:
	docker build . -t volley_api:0.1 
clean:
	rm -rf __pycache__
