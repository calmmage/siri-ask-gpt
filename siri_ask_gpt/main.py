# app.py
from fastapi import FastAPI

app = FastAPI()

@app.post("/ask_gpt")
def read_root():
    return {"Hello": "World"}

@app.get("/ask_gpt")
def read_root():
    return {"Hello": "World"}
#
# if __name__ == '__main__':
#     uvicorn app:app --reload
