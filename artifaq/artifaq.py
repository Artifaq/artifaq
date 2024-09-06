import pretty_errors
from dependency_injector import containers, providers
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from artifaq.configs.config_manager import ConfigManager

# Configure pretty_errors for enhanced error display
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


class Artifaq(containers.DeclarativeContainer):
    """
    Artifaq class extends FastAPI to implement a singleton design pattern
    and provides custom configurations, CORS handling, and application management.
    """

    # Configuration providers
    app_config = providers.Configuration()
    cors_config = providers.Configuration()

    # Application providers
    app = providers.Singleton(
        FastAPI,
        title=app_config.get,
        description=config.app.description,
        version=config.app.version,
        debug=config.app.debug,
        docs_url=config.app.docs_url,
        redoc_url=config.app.redoc_url,
        openapi_url=config.app.openapi_url,
    )

    def __init__(self):
        super().__init__()
        self.app_config.override()


