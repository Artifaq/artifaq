from fastapi import FastAPI

from artifaq.core.bootstrap import Bootstrap
from artifaq.core.dependancy_injection import Container


def artifaq() -> FastAPI:
    container = Container()
    container.wire(modules=["my_fastapi_framework.api"])

    bootstrap = Bootstrap()
    bootstrap.setup()

    app = bootstrap.get_application()
    app.container = container

    return app