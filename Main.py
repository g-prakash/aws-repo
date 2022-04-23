from fastapi import FastAPI
from typing import Optional
#from fastapi_health import health

print("Hello World check")
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hellow": "World"}

