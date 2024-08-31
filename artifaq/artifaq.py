import sys
from typing import List, Dict, Any
import importlib.util
import os

from fastapi import FastAPI


class Artifaq(FastAPI):
    config: Dict[str, Any]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = {}
        self.load_configs()

    def load_configs(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(sys.argv[0]))

        config_dir = os.path.join(application_path, 'config')

        if not os.path.exists(config_dir):
            print(f"Le dossier de configuration n'existe pas : {config_dir}")
            return

        for filename in os.listdir(config_dir):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                file_path = os.path.join(config_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, 'config'):
                    self.config[module_name] = module.config
                else:
                    print(f"Aucune variable 'config' trouvée dans {filename}")

    def load_apps(self, apps_dir='apps'):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(sys.argv[0]))

        full_apps_dir = os.path.join(application_path, apps_dir)

        if not os.path.exists(full_apps_dir):
            print(f"Le dossier des applications n'existe pas : {full_apps_dir}")
            return

        for app_name in os.listdir(full_apps_dir):
            app_dir = os.path.join(full_apps_dir, app_name)
            if os.path.isdir(app_dir):
                router_path = os.path.join(app_dir, 'router.py')
                if os.path.exists(router_path):
                    spec = importlib.util.spec_from_file_location(f"{app_name}.router", router_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    if hasattr(module, "router"):
                        self.include_router(module.router)
                    else:
                        print(f"Aucun router trouvé dans {router_path}")
                else:
                    print(f"Fichier router.py non trouvé pour l'application {app_name}")
