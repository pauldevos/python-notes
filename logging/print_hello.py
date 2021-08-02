import logging

logger = logging.getLogger(__name__)

def hello():
    logger.debug("this is debug in Print Hello module")
    print("Hello!!!")


hello()