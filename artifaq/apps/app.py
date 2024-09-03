import importlib
import inspect
from typing import List, Type
from pydantic import BaseModel

from artifaq.apps.router import BaseRouter


class Application:
    def __init__(self, app_name: str, app_config: BaseModel):
        self.app_name = app_name
        self.configs: BaseModel = app_config
        self.routers: List[Type[BaseRouter]] = []

        from artifaq.logger import Logger
        self.logger = Logger()
        self.logger.info(f"Loaded application '{app_name}'")

        self._import_routers()


    def get_config(self, config_name: str) -> BaseModel:
        return self.configs.get(config_name)

    def _import_routers(self):
        try:
            router_module = importlib.import_module(f"apps.{self.app_name}.router")

            for name, obj in inspect.getmembers(router_module):
                if inspect.isclass(obj) and issubclass(obj, BaseRouter) and obj != BaseRouter:
                    self.routers.append(obj)
                    self.logger.info(f"Loaded router '{name}' for application '{self.app_name}'")

        except ImportError:
            self.logger.warning(f"No router.py file found for application '{self.app_name}'")
        except Exception as e:
            self.logger.error(f"Error loading routers for application '{self.app_name}': {str(e)}")

    def get_routers(self) -> List[Type[BaseRouter]]:
        return self.routers