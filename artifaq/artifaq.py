from fastapi import FastAPI

from artifaq.config_manager import ConfigManager

import pretty_errors

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
        self.init_config()

        self.init_cors()

    def init_config(self):
        from artifaq.interfaces.corsconfig import CORSConfig

        self.config_manager.register_interface("cors", CORSConfig)

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

