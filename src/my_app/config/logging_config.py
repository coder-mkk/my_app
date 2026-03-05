import logging
import logging.handlers
import sys
from pathlib import Path

from my_app.config import settings


def setup_logging(app_name="MyApp"):
    """
    Sets up logging to console (INFO+) and file (DEBUG+).
    Logs are saved to user's home directory: ~/.my_app/logs/app.log
    """
    # 1. Define Log Directory
    log_dir = Path.home() / f".{app_name.lower()}" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"

    # 2. Create Root Logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Clear existing handlers to avoid duplicates if called twice
    if logger.hasHandlers():
        logger.handlers.clear()

    # 3. Define Formatters
    file_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_fmt = logging.Formatter("%(levelname)s: %(message)s")

    # 4. File Handler (Rotating: 1MB size, keep last 5 files)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=1_048_576, backupCount=5, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_fmt)
    logger.addHandler(file_handler)

    # 5. Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(settings.LOG_LEVEL)
    console_handler.setFormatter(console_fmt)
    logger.addHandler(console_handler)

    logging.info(f"Logging initialized. Log file: {log_file}")
