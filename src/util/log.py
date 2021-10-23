import logging


class Logger:
    def __init__(self):
        logging.basicConfig(format='%(name)s - %(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def debug(self, message):
        logging.debug(message)

    def error(self, message):
        logging.error(message)