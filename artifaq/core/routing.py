from fastapi import APIRouter
from typing import Any, Callable, List, Type

class BaseRouter:
    def __init__(self, prefix: str = ""):
        self.router = APIRouter(prefix=prefix)

    def route(self, path: str, methods: List[str]):
        def decorator(func: Callable) -> Callable:
            self.router.add_api_route(path, func, methods=methods)
            return func
        return decorator

    def get(self, path: str):
        return self.route(path, ["GET"])

    def post(self, path: str):
        return self.route(path, ["POST"])

    def put(self, path: str):
        return self.route(path, ["PUT"])

    def delete(self, path: str):
        return self.route(path, ["DELETE"])

def include_routers(app: Any, routers: List[Type[BaseRouter]]):
    for router_class in routers:
        router_instance = router_class()
        app.include_router(router_instance.router)