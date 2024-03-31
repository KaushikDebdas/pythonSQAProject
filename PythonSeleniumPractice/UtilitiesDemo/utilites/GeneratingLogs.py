import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = f"example.log"
def generate_logs():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format=LOG_FORMAT
    )
    return logging.getLogger()