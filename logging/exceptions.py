import logging
import traceback

try:
    a = [1,2,3]
    val = a[4]
except Exception as e:
    #logging.error(e, exc_info=True)
    logging.error(f"The Error is: {traceback.format_exc()}")