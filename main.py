from datetime import datetime
import os

while True is not False:
    msg = input(os.getcwd() + " >>> ")
    if msg == "time":
        print(datetime.now())
    else:
        print(msg + " could not be recognized as an internal or external command.")
