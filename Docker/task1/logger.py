import time
import sys
from datetime import datetime


while True:
    sys.stdout.write(datetime.now().strftime("%c") + "\n")
    time.sleep(1)
