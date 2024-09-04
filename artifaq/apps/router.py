from fastapi import APIRouter, Depends
from typing import Any, Callable, List, Type

"""
Helper function to check if an object is a FastAPI dependency.

Args:
    obj: The object to check.

Returns:
    True if the object is a FastAPI dependency, False otherwise.
"""
def is_fastapi_dependency(obj: Any) -> bool:
    return callable(obj) and hasattr(obj, "__dependencies__")

"""
Decorator to add a prefix and tags to a router class.

Args:
    prefix: The prefix to add to the router.
    tags: A list of tags to add to the router.

Returns:
    A decorator that can be used to decorate a router class.
"""
def router_config(prefix: str, tags: List[str]):
    def decorator(cls: Type[Any]):
        cls._prefix = prefix
        cls._tags = tags
        return cls
    return decorator

"""
Base class for routers.
"""
class RouterBase:
    """
    Gets the router for the class.

    Returns:
        The router for the class.
    """
    @classmethod
    def get_router(cls) -> APIRouter:
        # Create an APIRouter with the prefix and tags from the class
        router = APIRouter(prefix=cls._prefix, tags=cls._tags)

        # Iterate over the methods of the class to register the routes
        for name, method in cls.__dict__.items():
            if hasattr(method, "__route_info__"):
                path, http_method = method.__route_info__

                # Add the route to the FastAPI router
                router.add_api_route(path, method, methods=[http_method])

        return router

"""
Decorators for the different HTTP methods.
"""
class router:
    """
    Decorator for GET requests.

    Args:
        path: The path of the route.

    Returns:
        A decorator that can be used to decorate a function.
    """
    @staticmethod
    def get(path: str):
        def decorator(func: Callable):
            func.__route_info__ = (path, "GET")
            return func
        return decorator

    """
    Decorator for POST requests.

    Args:
        path: The path of the route.

    Returns:
        A decorator that can be used to decorate a function.
    """
    @staticmethod
    def post(path: str):
        def decorator(func: Callable):
            func.__route_info__ = (path, "POST")
            return func
        return decorator

    """
    Decorator for PUT requests.

    Args:
        path: The path of the route.

    Returns:
        A decorator that can be used to decorate a function.
    """
    @staticmethod
    def put(path: str):
        def decorator(func: Callable):
            func.__route_info__ = (path, "PUT")
            return func
        return decorator

    """
    Decorator for DELETE requests.

    Args:
        path: The path of the route.

    Returns:
        A decorator that can be used to decorate a function.
    """
    @staticmethod
    def delete(path: str):
        def decorator(func: Callable):
            func.__route_info__ = (path, "DELETE")
            return func
        return decorator