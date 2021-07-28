import logging
# https://docs.python.org/3/library/logging.handlers.html
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time

logger  = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs...
handler_size = RotatingFileHandler('app.log', mode='a', maxBytes=2000, backupCount=5)

# when: s, m, h, d, midnight, w0
handler_time = TimedRotatingFileHandler('timed_log.log', when='s', interval=5, backupCount=5)


logger.addHandler(handler_time)

for _ in range(20):
    time.sleep(1)
    logger.info("This is some text, watch it pile up over time.")