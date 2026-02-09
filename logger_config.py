# logger_config.py

import logging
import os

PROJECT_FOLDER = "/home/sakshi-asati/Desktop/python/Mini_project"
LOG_FILE = os.path.join(PROJECT_FOLDER, "project_log.txt")

def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a"   # append mode
    )
    logging.info("===== Application Started =====")
