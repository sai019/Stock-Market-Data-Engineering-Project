import logging
import os
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from src.config import LOG_DIR

log_dir = LOG_DIR
log_filename = datetime.now().strftime("%d-%m-%Y-%H_%M_%S.log")
log_filepath = os.path.join(log_dir, log_filename)
os.makedirs(log_dir, exist_ok=True)
# with open(log_filepath, "a") as log_file:
# log_file.write("=" * 200 + "\n")


FORMAT = "[%(asctime)s] %(levelname)s: %(message)s (Filename: [%(filename)s] -> Line: %(lineno)d)"


file_handler = TimedRotatingFileHandler(
    log_filepath,
    when="midnight",
    interval=1,
    backupCount=1,  # Keep up to 7 days of logs
    encoding="utf-8",
)

file_handler.setFormatter(logging.Formatter(FORMAT))

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="%d/%m/%Y - %I:%M:%S %p",
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)
