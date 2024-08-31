from typing import List
import importlib.util
import os

from fastapi import FastAPI


class Artifaq(FastAPI):
    config: List

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_configs()
        # self.load_apps(apps)

    def load_apps(self, app_paths: List[str]):
        for path in app_paths:
            if not os.path.exists(path):
                print(f"Le chemin {path} n'existe pas.")
                continue

            module_name = os.path.basename(path).replace(".py", "")
            spec = importlib.util.spec_from_file_location(module_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "router"):
                self.include_router(module.router)
            else:
                print(f"Aucun router trouvé dans {path}")

    def load_configs(self):
        pass