import logging
import os
from flask import request


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        # Add endpoint info if request exists
        try:
            record.endpoint = request.path
            record.method = request.method
        except RuntimeError:
            record.endpoint = "N/A"
            record.method = "N/A"

        return super().format(record)


def get_logger():
    logger = logging.getLogger("my_app")

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        formatter = RequestFormatter(
            "%(asctime)s | %(levelname)s | %(method)s %(endpoint)s | %(message)s"
        )

        # File: app.log
        file_handler = logging.FileHandler(os.path.join(LOG_DIR, "app.log"))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # File: error.log
        error_handler = logging.FileHandler(os.path.join(LOG_DIR, "error.log"))
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)

        # Console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(error_handler)
        logger.addHandler(console_handler)

    return logger