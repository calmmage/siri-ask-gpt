# app.py
from dotenv import load_dotenv
from fastapi import FastAPI

from siri_ask_gpt.app_config import AppConfig

load_dotenv()

app = FastAPI()
app_config = AppConfig()


@app.post("/ask-gpt")
def read_root():
    return {"Hello": "World"}


@app.get("/ask-gpt")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=app_config.host, port=app_config.port)
