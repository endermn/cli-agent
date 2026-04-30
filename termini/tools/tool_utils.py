import logging

from termini.services.logger import terminiLogger

logger: logging.Logger = terminiLogger(name=__name__, file="termini.log").get_logger()
