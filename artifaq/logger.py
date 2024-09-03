import logging
import os
from pickle import PROTO

from artifaq.artifaq import Artifaq


class Logger(logging.Logger):
    def __init__(self):
        super().__init__("artifaq")

        print(Artifaq().config_manager.config['app'])
        self.config = Artifaq().config_manager.config["app"]

        if self.config['logs_enabled']:
            self._setup_logger()

    def _setup_logger(self):
        if not os.path.exists(self.config["logs_dir"]):
            os.makedirs(self.config['logs_dir'])

        level = getattr(logging, self.config["logs_level"].upper())
        self.setLevel(level)

        file_handler = logging.FileHandler(os.path.join(self.config["logs_dir"], self.config["logs_file"]))
        file_handler.setLevel(level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        formatter = logging.Formatter(self.config["logs_format"])

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.addHandler(file_handler)
        self.addHandler(console_handler)