import logging
import time
import os

def init_logger():
   # Create a formatter with a custom date and time format
    formatter = logging.Formatter('[%(asctime)s] | [%(levelname)s] | [%(pathname)s] | %(message)s', datefmt='%Y-%m-%d %H:%M:%S UTC')
    formatter.converter = time.gmtime

    # Create a stream handler and set the formatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Create a logger instance for common package
    logger = logging.getLogger(__name__)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)

    return logger

print("test" + __name__)