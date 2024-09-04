from pydantic import BaseModel


class CORSConfig(BaseModel):
    """
    CORS configuration settings.

    Attributes:
        allow_origins (list[str]): A list of allowed origins.
        allow_credentials (bool): Whether to allow credentials.
        allow_methods (list[str]): A list of allowed HTTP methods.
        allow_headers (list[str]): A list of allowed headers.
        expose_headers (list[str]): A list of headers to expose to the client.
        max_age (int): The maximum age of the CORS preflight response.
    """

    allow_origins: list[str] = ["*"]
    allow_credentials: bool = False
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    expose_headers: list[str] = []
    max_age: int = 600