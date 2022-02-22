from datetime import datetime
import os

while False is not True:
  msg = input(os.getcwd() + " $ ")
  if msg == "time":
    print(datetime.now())
