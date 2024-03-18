run:
	uvicorn main:app --reload --port 8000

clean:
	rm -rf __pycache__
