import os
from fastapi import FastAPI
from artifaq.apps.app import Application
from artifaq.config_manager import ConfigManager
import pretty_errors
from typing import Dict
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
        self._init_config()
        self._init_cors()
        self._load_applications()

    def _init_config(self):
        from artifaq.interfaces.corsconfig import CORSConfig
        from artifaq.interfaces.appconfig import APPConfig

        self.config_manager.register_interface("cors", CORSConfig)
        self.config_manager.register_interface("app", APPConfig)

        self.config_manager.load_configs()

    def _init_cors(self):
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


    def _load_applications(self):
        apps_dir = "apps"
        for app_name in os.listdir(apps_dir):
            app_dir = os.path.join(apps_dir, app_name)
            if os.path.isdir(app_dir):
                try:
                    from artifaq.utils.load_app_config import load_app_config
                    from artifaq.utils.load_app_interface import load_app_interface

                    app_interface = load_app_interface(app_name)
                    app_config = load_app_config(app_name, app_interface)
                    self.register_application(app_name, app_config)
                except (ConfigurationError, InterfaceError) as e:
                    raise ApplicationLoadError(f"Failed to load application '{app_name}': {str(e)}")

    def register_application(self, app_name: str, app_config: BaseModel):
        app_instance = Application(app_name, app_config)

        for router in app_instance.get_routers():
            self.include_router(router.get_router())

        self.applications[app_name] = app_instance

    def get_application(self, app_name: str) -> Application:
        return self.applications.get(app_name)

    def list_applications(self) -> list:
        return list(self.applications.keys())