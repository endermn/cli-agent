import logging

from termini.services.logger import FileLogger

logger: logging.Logger = FileLogger(name=__name__, file="termini.log").get_logger()
