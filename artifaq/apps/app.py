from typing import Type
from pydantic import BaseModel

class Application:
    def __init__(self, app_name: str, app_config: BaseModel):
        self.app_name = app_name
        self.configs: BaseModel = app_config
        from artifaq.logger import Logger
        Logger().info(f"Loaded application '{app_name}'")

    def get_config(self, config_name: str) -> BaseModel:
        return self.configs.get(config_name)

    def get_model(self, model_name: str) -> Type[BaseModel]:
        return self.models.get(model_name)