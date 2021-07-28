import logging

logging.basicConfig(level=logging.DEBUG, filename='logging.txt', 
                    filemode='a',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt='%m/%d/%Y %H:%M:%S'
                    )


logging.debug("This is a debug message")
logging.info("This is an info message")
# these logged by default, can set a level higher like debug if desired.
logging.warning("this is a warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")