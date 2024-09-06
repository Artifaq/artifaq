from fastapi import FastAPI
from dependency_injector.wiring import inject, Provide

from artifaq.config.app_config import AppConfig
from artifaq.config.project_config import ProjectConfig
from artifaq.core.dependancy_injection import Container


class Bootstrap:
    @inject
    def __init__(
            self,
            app_config: AppConfig = Provide[Container.config.app_config],
            project_config: ProjectConfig = Provide[Container.config.project_config]
    ):
        self.app_config = app_config
        self.project_config = project_config
        self.app = FastAPI(title=self.project_config.name, version=self.project_config.version)

    def setup(self):
        self._setup_middlewares()
        self._setup_routes()
        self._setup_exception_handlers()

    def _setup_middlewares(self):
        # Ajoutez ici la configuration des middlewares
        pass

    def _setup_routes(self):
        # Importez et ajoutez ici vos routes
        pass

    def _setup_exception_handlers(self):
        # Ajoutez ici la configuration des gestionnaires d'exceptions
        pass

    def get_application(self) -> FastAPI:
        return self.app