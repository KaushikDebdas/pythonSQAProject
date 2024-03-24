import logging
from datetime import datetime

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = f"D:/Study Videos/Python/pythonProject/SampleProject3_POM/tests/demofile44.log"

def log_details():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format=LOG_FORMAT
    )
    return logging.getLogger()

# logger = log_details()

# a =4
# b =3
# if a>b:
#     print("Kaushik")
#     logger.info("a is greater than b, hence Kaushik got printed in output")
#
# logger.info("Execution stop")