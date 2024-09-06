from dependency_injector import containers, providers

from artifaq.config.app_config import AppConfig
from artifaq.config.project_config import ProjectConfig
from artifaq.database.base import get_db


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["my_fastapi_framework.api"])

    config = providers.Configuration()

    db = providers.Callable(get_db)

    app_config = providers.Singleton(AppConfig)
    project_config = providers.Singleton(ProjectConfig)

    # Ajoutez ici vos services et repositories
    # example_service = providers.Factory(ExampleService, repository=example_repository)