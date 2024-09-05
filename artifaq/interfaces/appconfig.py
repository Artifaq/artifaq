from pydantic import BaseModel

class APPConfig(BaseModel):
    """
    Application configuration settings.

    Attributes:
        mode (str): The application mode (e.g., 'development', 'production').
        debug (bool): Whether the application should run in debug mode.
        logs_dir (str): The directory where log files will be stored.
        logs_enabled (bool): Whether logging is enabled.
        logs_level (str): The logging level (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        logs_format (str): The logging format string.
        logs_file (str): The name of the log file.
    """

    apps: list[str] = []
    mode: str = 'development'
    debug: bool = True
    logs_dir: str = 'logs'
    logs_enabled: bool = True
    logs_level: str = 'DEBUG'
    logs_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logs_file: str = 'app.log'