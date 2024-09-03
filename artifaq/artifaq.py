import os
from fastapi import FastAPI
from pydantic import ValidationError
from artifaq.apps.app import Application
from artifaq.config_manager import ConfigManager
import pretty_errors
from typing import Dict, Type
from importlib import import_module
from pydantic import BaseModel

from artifaq.errors.ArtifaqError import ConfigurationError, InterfaceError, ApplicationLoadError

pretty_errors.configure(
    separator_character="*",
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_number_first=True,
    display_link=True,
    lines_before=5,
    lines_after=2,
    line_color=pretty_errors.RED + "> " + pretty_errors.default_config.line_color,
    code_color="  " + pretty_errors.default_config.line_color,
    truncate_code=True,
    display_locals=True,
)


class Artifaq(FastAPI):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Artifaq, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, *args, **kwargs):
        if self.__initialized:
            return
        super().__init__(*args, **kwargs)
        self.__initialized = True
        self.config_manager = ConfigManager()
        self.applications: Dict[str, Application] = {}
        self.init_config()
        self.init_cors()
        self.load_applications()

    def init_config(self):
        from artifaq.interfaces.corsconfig import CORSConfig
        from artifaq.interfaces.appconfig import APPConfig

        self.config_manager.register_interface("cors", CORSConfig)
        self.config_manager.register_interface("app", APPConfig)

        self.config_manager.load_configs()

    def init_cors(self):
        from fastapi.middleware.cors import CORSMiddleware

        self.add_middleware(
            CORSMiddleware,
            allow_origins=self.config_manager.config["cors"]["allow_origins"],
            allow_credentials=self.config_manager.config["cors"]["allow_credentials"],
            allow_methods=self.config_manager.config["cors"]["allow_methods"],
            allow_headers=self.config_manager.config["cors"]["allow_headers"],
            expose_headers=self.config_manager.config["cors"]["expose_headers"],
            max_age=self.config_manager.config["cors"]["max_age"],
        )


    def load_applications(self):
        apps_dir = "apps"
        for app_name in os.listdir(apps_dir):
            app_dir = os.path.join(apps_dir, app_name)
            if os.path.isdir(app_dir):
                try:
                    app_interface = self.load_app_interface(app_name)
                    app_config = self.load_app_config(app_name, app_interface)
                    app_instance = Application(app_name, app_config)
                    self.applications[app_name] = app_instance
                except (ConfigurationError, InterfaceError) as e:
                    raise ApplicationLoadError(f"Failed to load application '{app_name}': {str(e)}")

    def load_app_config(self, app_name: str, interface_class: Type[BaseModel]) -> BaseModel:
        try:
            config_module = import_module(f"config.apps.{app_name}")
            raw_config = getattr(config_module, "config")
            validated_config = interface_class(**raw_config)
            return validated_config
        except ImportError:
            raise ConfigurationError(f"No configuration found for application '{app_name}'")
        except ValidationError as e:
            raise ConfigurationError(f"Validation error for configuration of '{app_name}': {e}")

    def load_app_interface(self, app_name: str) -> Type[BaseModel]:
        try:
            interface_module = import_module(f"apps.{app_name}.config")
            return getattr(interface_module, f"{app_name.capitalize()}Config")
        except ImportError:
            raise InterfaceError(f"No interface found for application '{app_name}'")
        except AttributeError:
            raise InterfaceError(f"Invalid interface definition for application '{app_name}'")

    def get_application(self, app_name: str) -> Application:
        return self.applications.get(app_name)

    def list_applications(self) -> list:
        return list(self.applications.keys())