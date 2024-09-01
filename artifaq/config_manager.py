import importlib
import sys
from pathlib import Path
from typing import Dict, Any, Type

from pydantic import BaseModel


class ConfigManager:
    def __init__(self):
        self.config_dir = Path(sys.path[0]) / "config"
        self.config: Dict[str, Any] = {}
        self.interfaces: Dict[str, Type[BaseModel]] = {}

    def register_interface(self, name: str, interface: Type[BaseModel]):
        self.interfaces[name] = interface

    def register_config(self, name: str, config: Dict[str, Any]):
        if name not in self.interfaces:
            import logging
            logging.error(f"Interface '{name}' not registered")
            return
        validated_config = self.interfaces[name](**config)
        self.config[name] = validated_config.dict()

    def load_configs(self):
        if not self.config_dir.exists():
            raise FileNotFoundError(f"Config directory not found: {self.config_dir}")

        for config_file in self.config_dir.glob("*.py"):
            name = config_file.stem
            spec = importlib.util.spec_from_file_location(name, config_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "config"):
                self.register_config(name, module.config)
            else:
                print(f"Warning: No 'config' variable found in {config_file}")