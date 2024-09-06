from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        env_prefix = "APP_"