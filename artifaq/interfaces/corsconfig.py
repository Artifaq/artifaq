from pydantic import BaseModel


class CORSConfig(BaseModel):
    allow_origins: list[str] = ["*"]
    allow_credentials: bool = False
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    expose_headers: list[str] = []
    max_age: int = 600