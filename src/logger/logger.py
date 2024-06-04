import logging
import os
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

script_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
log_dir = os.path.join(project_root, "logs")
# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)
log_filename = datetime.now().strftime("%d-%m-%Y-%H_%M_%S.log")
log_filepath = os.path.join(log_dir, log_filename)
# with open(log_filepath, "a") as log_file:
# log_file.write("=" * 200 + "\n")


FORMAT = "[%(asctime)s] %(levelname)s: %(message)s (Filename: [%(filename)s] -> Line: %(lineno)d)"


file_handler = TimedRotatingFileHandler(
    log_filepath,
    when="midnight",
    interval=1,
    backupCount=7,  # Keep up to 7 days of logs
    encoding="utf-8",
)

file_handler.setFormatter(logging.Formatter(FORMAT))

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="%d/%m/%Y - %I:%M:%S %p",
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)
