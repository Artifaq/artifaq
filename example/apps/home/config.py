from pydantic import BaseModel

class HomeConfig(BaseModel):
    title: str = 'Home'
    description: str = 'Welcome to the home page'
    keywords: str = 'home, welcome, page'
