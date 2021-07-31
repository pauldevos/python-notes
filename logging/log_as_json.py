import json
import traceback
from datetime import datetime

def addLogging(logDict:dict):
    loggingsFile = 'loggings.json'

    with open(loggingsFile) as f:
        data = json.load(f)

    data.append(logDict)

    with open(loggingsFile, 'w') as f:
        json.dump(data, f)

def currentTimeUTC():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

try:
    print(5 / 0)
except ZeroDivisionError:
    fullTraceback = str(traceback.format_exc())
    addLogging({'timestamp': currentTimeUTC(), 'level': 'error', 'traceback': fullTraceback})