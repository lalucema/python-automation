# utils/logger.py
import logging
import os
import colorlog

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_dir, exist_ok=True)

logger = logging.getLogger("automation_logger")
logger.setLevel(logging.INFO)

# ----------------------------------------------------------------------
# 🚀 THE IMPORTANT FIX: block reinitialization forever
# ----------------------------------------------------------------------
if getattr(logger, "initialized", False) is False:

    # ---------------- Console Handler ----------------
    console_handler = colorlog.StreamHandler()
    console_handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s[%(asctime)s][%(levelname)s] %(message)s",
            log_colors={
                "DEBUG": "green",
                "INFO": "cyan",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
            datefmt="%m-%d-%Y %I:%M:%S %p"
        )
    )
    logger.addHandler(console_handler)

    # ---------------- File Handler ----------------
    file_handler = logging.FileHandler(
        os.path.join(logs_dir, "automation.log"),
        encoding="utf-8"
    )
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s][%(levelname)s] %(message)s",
            datefmt="%m-%d-%Y %I:%M:%S %p"
        )
    )
    logger.addHandler(file_handler)

    # IMPORTANT: mark logger as initialized  
    logger.initialized = True

automation_logger = logger
