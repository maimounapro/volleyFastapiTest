# creation d'une environnement virtuel
python -m venv path/to/my/env
source path/to/my/env/bin/activate

# installer les requirements
pip install -r requirements.txt

# lauch API
uvicorn main:app --reload