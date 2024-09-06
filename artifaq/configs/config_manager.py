import json


class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = None

    def load_config(self):
        with open(self.config_path, "r") as f:
            self.config = json.load(f)

    def get_config(self):
        return self.config

    def get_config_value(self, key: str):
        return self.config[key]

    def set_config_value(self, key: str, value):
        self.config[key] = value

    def save_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.config, f)