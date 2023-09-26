import datetime as dt
import time

for i in range(5):
    i = dt.datetime.now()
    print(i.strftime("%H:%M:%S"))
    time.sleep(1)