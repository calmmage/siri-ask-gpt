from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    openai_api_key: str
    host: str = "localhost"
    port: int = 8000
    default_model: str = "gpt-3.5-turbo"
    default_max_tokens: int = 1000
