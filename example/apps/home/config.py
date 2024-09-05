from pydantic import BaseModel

class HomeConfig(BaseModel):
    __app_name__: str = 'home'

    title: str = 'Home'
    description: str = 'Welcome to the home page'
    keywords: str = 'home, welcome, page'
