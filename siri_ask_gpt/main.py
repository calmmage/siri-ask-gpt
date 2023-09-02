import base64
from typing import Optional

import openai
from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger

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
            max_tokens: Optional[int] = None, is_encoded=False) -> str:
    """
    Fetches a response from the GPT model based on the provided question.

    Args:
    - question (str): The query to be answered.
    - model (Optional[str]): The GPT model to use. Defaults to app's default model.
    - max_tokens (Optional[int]): Maximum number of tokens for the response. Defaults to app's setting.

    Returns:
    - str: The GPT model's response.
    """

    # Default values if not provided
    if not model:
        model = app_config.default_model
    if not max_tokens:
        max_tokens = app_config.default_max_tokens
    if is_encoded:
        # base64 decode question
        question = base64.b64decode(question).decode('utf-8')

    # Logging input details
    logger.info(
        f"Received question: {question} for model: {model} with max_tokens: {max_tokens}")

    # Constructing and sending request to OpenAI's GPT
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

    # Extracting response content
    gpt_response = response.choices[0]['message']['content']

    # Logging the response
    logger.info(f"Response from GPT: {gpt_response}")

    return gpt_response


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=app_config.host, port=app_config.port)
