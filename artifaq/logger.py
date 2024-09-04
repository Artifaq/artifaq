import logging
import os
from artifaq.artifaq import Artifaq


class Logger(logging.Logger):
    """
    Custom Logger class for the Artifaq application. It extends the built-in logging.Logger
    class to configure logging based on application configuration settings.

    Attributes:
        config (Dict): The application's logging configuration loaded from the Artifaq config manager.
    """

    def __init__(self):
        """
        Initialize the Logger. It retrieves logging settings from the application's config manager
        and sets up the logger if logging is enabled.
        """
        super().__init__("artifaq")

        # Get the logging configuration from the Artifaq application
        self.config = Artifaq().config_manager.config["app"]

        if self.config['logs_enabled']:
            self._setup_logger()

    def _setup_logger(self):
        """
        Set up the logger by configuring file and console handlers, setting log levels, and applying formatting.
        The log files will be stored in the directory specified by the configuration.
        """
        # Ensure the logs directory exists
        logs_dir = self.config.get("logs_dir", "logs")
        logs_file = self.config.get("logs_file", "app.log")

        if not os.path.exists(logs_dir):
            try:
                os.makedirs(logs_dir)
            except OSError as e:
                raise RuntimeError(f"Failed to create logs directory: {logs_dir}") from e

        # Get the logging level from configuration
        level = getattr(logging, self.config.get("logs_level", "INFO").upper(), logging.INFO)
        self.setLevel(level)

        # File handler for writing logs to a file
        file_handler = logging.FileHandler(os.path.join(logs_dir, logs_file))
        file_handler.setLevel(level)

        # Console handler for logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Log format
        formatter = logging.Formatter(self.config.get("logs_format", '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # Apply formatter to both handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.addHandler(file_handler)
        self.addHandler(console_handler)
