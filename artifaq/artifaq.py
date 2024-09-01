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

    def init_config(self):
        from artifaq.interfaces.corsconfig import CORSConfig

        self.config_manager.register_interface("cors", CORSConfig)

        self.config_manager.load_configs()
