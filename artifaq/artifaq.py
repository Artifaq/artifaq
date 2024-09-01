from fastapi import FastAPI

from artifaq.config_manager import ConfigManager


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

