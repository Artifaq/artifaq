import importlib
import inspect
from typing import List, Type
from pydantic import BaseModel
from fastapi import APIRouter

from artifaq.apps.router import RouterBase


"""
Main application class for ArtiFAQ.

This class handles application configuration, router loading, and configuration retrieval.
"""
class Application:
    """
    Initializes the application instance.

    Args:
        app_name (str): The name of the application.
        app_config (BaseModel): The application configuration object.
    """
    def __init__(self, app_name: str, app_config: BaseModel):
        self.app_name = app_name
        self.configs: BaseModel = app_config
        self.routers: List[APIRouter] = []

        from artifaq.logger import Logger
        self.logger = Logger()
        self.logger.info(f"Loaded application '{app_name}'")

        self._import_routers()

    """
    Retrieves a specific configuration value from the application configuration object.

    Args:
        config_name (str): The name of the configuration value to retrieve.

    Returns:
        BaseModel: The configuration value associated with the provided name, or None if not found.
    """
    def get_config(self, config_name: str) -> BaseModel:
        return self.configs.get(config_name)

    """
    Internal helper method to import routers from the application's router module.

    This method attempts to import the `router.py` file from the application's router directory
    and iterate over its classes, registering any that are subclasses of `RouterBase`.
    """
    def _import_routers(self):
        try:
            router_module = importlib.import_module(f"apps.{self.app_name}.router")

            for name, obj in inspect.getmembers(router_module):
                if inspect.isclass(obj) and issubclass(obj, RouterBase) and obj != RouterBase:
                    self.routers.append(obj)
                    self.logger.info(f"Loaded router '{name}' for application '{self.app_name}'")

        except ImportError:
            self.logger.warning(f"No router.py file found for application '{self.app_name}'")
        except Exception as e:
            self.logger.error(f"Error loading routers for application '{self.app_name}': {str(e)}")

    """
    Retrieves a list of all registered routers for the application.

    Returns:
        List[Type[RouterBase]]: A list of all the registered `RouterBase` subclasses.
    """
    def get_routers(self) -> List[Type[RouterBase]]:
        return self.routers