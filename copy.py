import shutil
import time
from datetime import datetime

nameProyect = 'test'

while True:
    now = datetime.now()
    date_time = now.strftime(" %m_%d_%Y %H_%M_%S")
    print("date and time:", date_time)
    shutil.copytree('d:/Desktop/'+nameProyect,
                    'd:/Desktop/copias/'+nameProyect+date_time)
    time.sleep(120)
