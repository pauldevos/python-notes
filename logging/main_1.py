import logging

import logging.config

logging.config.fileConfig('/path/to/logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

