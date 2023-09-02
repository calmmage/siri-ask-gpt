# app.py
from typing import Optional

import openai
from dotenv import load_dotenv
from fastapi import FastAPI

from siri_ask_gpt.app_config import AppConfig

load_dotenv()

app = FastAPI()
app_config = AppConfig()
openai.api_key = app_config.openai_api_key


@app.get("/")
def read_root():
    # describe api handles
    return {
        "handles": {
            "/ping-post": "POST ping",
            "/ping-get": "GET ping",
            "/ask-gpt": "POST ask gpt - ask a question to gpt, ",
        }
    }


@app.post("/ping-post")
def ping_post():
    return {"Hello": "World"}


@app.get("/ping-get")
def ping_get():
    return {"Hello": "World"}


@app.get("/ask-gpt")
def ask_gpt(question: str, model: Optional[str] = None,
            max_tokens: Optional[int] = None):
    if not model:
        model = app_config.default_model
    if not max_tokens:
        max_tokens = app_config.default_max_tokens

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You're an assistant responding to a voice query. "
                           "Try to be concise and informative",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        max_tokens=max_tokens,
    )

    return response.choices[0]['message']['content']


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=app_config.host, port=app_config.port)
