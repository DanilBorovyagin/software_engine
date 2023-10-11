import csv
import datetime
import time

try:
    with open("rows_300.csv", "x"):
        pass
except FileExistsError:
    with open("rows_300.csv", "w", encoding="utf-8", newline="") as f:
        wri = csv.writer(f)
        wri.writerow(["№","секунда","микросекунда"])
        for line in range(0,300):
            wri.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
            time.sleep(0.01)
