from pydantic import BaseModel

class TestConfig(BaseModel):
    __app_name__: str = 'test'
