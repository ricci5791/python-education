import time
from datetime import datetime

while True:
    print(datetime.now().strftime("%c"))
    time.sleep(1)
