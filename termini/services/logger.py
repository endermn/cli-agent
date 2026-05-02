import logging


class FileLogger():
    logger: logging.Logger
    formatter: logging.Formatter

    def __init__(self, name: str, file: str, level=logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        self.logger.propagate = False

        file_handler = logging.FileHandler(file, mode='w')
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger



