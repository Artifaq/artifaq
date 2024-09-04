import importlib
import sys
from pathlib import Path
from typing import Dict, Any, Type

from pydantic import BaseModel


class ConfigManager:
    """
    ConfigManager is responsible for managing the application's configurations.
    It loads configuration files, validates them against registered interfaces,
    and stores the validated configurations.

    Attributes:
        config_dir (Path): Path to the directory where configuration files are stored.
        config (Dict[str, Any]): A dictionary holding the validated configurations.
        interfaces (Dict[str, Type[BaseModel]]): A dictionary mapping configuration names to their respective Pydantic model interfaces.
    """

    def __init__(self):
        """
        Initialize ConfigManager with the default configuration directory and empty configuration and interface dictionaries.
        """
        self.config_dir: Path = Path(sys.path[0]) / "config"
        self.config: Dict[str, Any] = {}
        self.interfaces: Dict[str, Type[BaseModel]] = {}

    def register_interface(self, name: str, interface: Type[BaseModel]):
        """
        Register a new interface for validating configuration files.

        Args:
            name (str): The name of the interface, typically related to the configuration it validates.
            interface (Type[BaseModel]): The Pydantic model class used for validation of the configuration.
        """
        self.interfaces[name] = interface

    def register_config(self, name: str, config: Dict[str, Any]):
        """
        Register and validate a configuration for a given name against the corresponding registered interface.

        Args:
            name (str): The name of the configuration to register.
            config (Dict[str, Any]): The raw configuration data to be validated.

        Raises:
            ValueError: If the interface for the provided name is not registered.
        """
        if name not in self.interfaces:
            import logging
            logging.error(f"Interface '{name}' not registered")
            raise ValueError(f"Interface '{name}' not registered")

        # Validate and store the config using the registered Pydantic model
        validated_config = self.interfaces[name](**config)
        self.config[name] = validated_config.model_dump()

    def load_configs(self):
        """
        Load all configuration files from the config directory and validate them
        using the registered interfaces. Only Python files with a 'config' variable
        will be processed.

        Raises:
            FileNotFoundError: If the configuration directory does not exist.
        """
        if not self.config_dir.exists():
            raise FileNotFoundError(f"Config directory not found: {self.config_dir}")

        # Iterate over Python files in the config directory
        for config_file in self.config_dir.glob("*.py"):
            name = config_file.stem
            spec = importlib.util.spec_from_file_location(name, config_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Check for the 'config' variable in the loaded module
            if hasattr(module, "config"):
                self.register_config(name, module.config)
            else:
                print(f"Warning: No 'config' variable found in {config_file}")
