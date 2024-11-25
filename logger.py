import logging
import os


class Logger:
    """
    Logger klasse
    """

    def __init__(self, name: str, log_level: int = logging.INFO):
        """
        Args:
            name (str): name of logger
            log_level (int): loglevel
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        # Create a file handler
        file_handler = logging.FileHandler("log.log")
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def info(self, message: str) -> None:
        """
        Log level info.

        Args:
            message (str): Log message.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Log level warning.

        Args:
            message (str): Log message.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Log level error.

        Args:
            message (str): Log message.
        """
        self.logger.error(message)

