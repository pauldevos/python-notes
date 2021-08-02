import logging
from print_hello import hello


# grabs the name of the file for the log message
# good practice to add to all modules
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Handlers: this is where the outputs go to:
# create a handler
stream_handler = logging.StreamHandler() # streams to the console
file_handler = logging.FileHandler('file.log')

# set level and format
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == 'main':
    print('main ran')
    hello()