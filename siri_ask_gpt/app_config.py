from pydantic import BaseSettings

class AppConfig(BaseSettings):
    # openai token
    openai_api_key: str
    host: str = ""
    port: int = 8000
