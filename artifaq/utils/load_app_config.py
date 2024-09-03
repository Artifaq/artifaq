from importlib import import_module
from typing import Type


from artifaq.errors.ArtifaqError import ConfigurationError
from pydantic import BaseModel, ValidationError


def load_app_config(app_name: str, interface_class: Type[BaseModel]) -> BaseModel:
    try:
        config_module = import_module(f"config.apps.{app_name}")
        raw_config = getattr(config_module, "config")
        validated_config = interface_class(**raw_config)
        return validated_config
    except ImportError:
        raise ConfigurationError(f"No configuration found for application '{app_name}'")
    except ValidationError as e:
        raise ConfigurationError(f"Validation error for configuration of '{app_name}': {e}")