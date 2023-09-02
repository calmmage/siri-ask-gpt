from pydantic import BaseSettings

class AppConfig(BaseSettings):
    # openai token
    openai_token: str
    host: str = ""
    port: int = 8000
