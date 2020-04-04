import math
import os
import sys
from os import register_at_fork

import requests

print(sys.executable)
r = requests.get("https://www.espn.com")
print(r.status_code)

test = "test"
