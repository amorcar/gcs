
To run the api server:

```
python3 -m venv venv --propmpt fastapi
source venv/bin/activate
pip install fastapi[all]
uvicorn app.main:app --reload  --reload-dir app
```