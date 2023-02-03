import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = 'mylogs_host_address.com'
PAPERTRAIL_PORT = 37554

def main() -> None:
    
    # logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('paulcodes')
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)
    logger.debug("This is a debg message")
    
    
if __name__ == '__main__':
    main()
    