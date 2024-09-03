from typing import Type, Dict, List
from importlib import import_module
from pydantic import BaseModel, ValidationError

class Application:
    def __init__(self, app_name: str, app_config: BaseModel):
        self.app_name = app_name
        self.configs: Dict[str, BaseModel] = {}
        self.models: Dict[str, Type[BaseModel]] = {}

        self._load_configs()
        self._load_models()

    def _load_configs(self):
        try:
            config_module = import_module(f"apps.{self.app_name}.config")
            for name, obj in config_module.__dict__.items():
                if isinstance(obj, type) and issubclass(obj, BaseModel) and obj != BaseModel:
                    try:
                        instance = obj()
                        self.configs[name] = instance
                    except ValidationError as e:
                        print(f"Erreur de validation pour la config {name}: {e}")
        except ImportError:
            print(f"Aucun module de configuration trouvé pour l'application {self.app_name}")

    def _load_models(self):
        try:
            models_module = import_module(f"apps.{self.app_name}.models")
            for name, obj in models_module.__dict__.items():
                if isinstance(obj, type) and issubclass(obj, BaseModel) and obj != BaseModel:
                    self.models[name] = obj
        except ImportError:
            print(f"Aucun module de modèles trouvé pour l'application {self.app_name}")

    def get_config(self, config_name: str) -> BaseModel:
        return self.configs.get(config_name)

    def get_model(self, model_name: str) -> Type[BaseModel]:
        return self.models.get(model_name)