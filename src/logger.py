import os
import logging
from logging.handlers import RotatingFileHandler

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, "app.log")

# Create a rotating log file handler
handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=1000000, backupCount=5)

# Create a formatter and attach it to the handler
formatter = logging.Formatter('[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Create a logger and attach the handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

