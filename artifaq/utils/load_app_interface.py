from importlib import import_module
from typing import Type

from artifaq.errors.ArtifaqError import InterfaceError
from pydantic import BaseModel


"""
Loads the configuration interface for a given application.

Args:
    app_name (str): The name of the application.

Returns:
    Type[BaseModel]: The Pydantic model class representing the configuration interface.

Raises:
    InterfaceError: If there's an error loading the interface.
"""
def load_app_interface(app_name: str) -> Type[BaseModel]:
    try:
        interface_module = import_module(f"apps.{app_name}.config")
        return getattr(interface_module, f"{app_name.capitalize()}Config")
    except ImportError:
        raise InterfaceError(f"No interface found for application '{app_name}'")
    except AttributeError:
        raise InterfaceError(f"Invalid interface definition for application '{app_name}'")