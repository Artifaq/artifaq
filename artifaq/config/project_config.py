from pydantic_settings import BaseSettings


class ProjectConfig(BaseSettings):
    name: str = "My FastAPI Extended Framework"
    version: str = "0.1.0"

    class Config:
        env_file = ".env"
        env_prefix = "PROJECT_"