from typing import Any, Callable, Dict, List, Type
from fastapi import APIRouter
from functools import wraps

def router_config(prefix: str = "", tags: List[str] = None):
    def decorator(cls: Type[BaseRouter]):
        cls._prefix = prefix
        cls._tags = tags or []
        return cls
    return decorator

def depends(func: Callable = None, **kwargs):
    if func is None:
        return lambda f: depends(f, **kwargs)

    @wraps(func)
    def wrapper(cls):
        cls._dependencies.update(kwargs)
        return func(cls)
    return wrapper

class RouterMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_cls = super().__new__(mcs, name, bases, attrs)
        router = new_cls.get_router()

        for attr_name, attr_value in attrs.items():
            if hasattr(attr_value, "__route_info__"):
                method, path = attr_value.__route_info__
                router.add_api_route(path, attr_value, methods=[method])

        return new_cls

def route(method: str, path: str):
    def decorator(func: Callable):
        func.__route_info__ = (method, path)
        return func
    return decorator

class router:
    @staticmethod
    def get(path: str):
        return route("GET", path)

    @staticmethod
    def post(path: str):
        return route("POST", path)

class BaseRouter(metaclass=RouterMeta):
    _router: APIRouter = None
    _prefix: str = ""
    _tags: List[str] = []
    _dependencies: Dict[str, Any] = {}

    @classmethod
    def get_router(cls) -> APIRouter:
        if cls._router is None:
            cls._router = APIRouter(prefix=cls._prefix, tags=cls._tags)
        return cls._router