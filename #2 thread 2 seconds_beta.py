# write: time every 2 seconds to a list
from datetime import datetime
import pytz 
import threading 
from threading import Thread

#define function 
def WRITE_n_SECONDS():
    #reapet_time 
    rpt_time = 2.0
    #start rep. timer
    threading.Timer(rpt_time, WRITE_n_SECONDS).start()
    dt_Rome = datetime.now(pytz.timezone('Europe/Rome'))
    print("Europe Rome DateTime:", dt_Rome.strftime("%Y-%m-%d %H:%M:%S %Z %z"))
    seconds = dt_Rome.strftime("%S")
    print(seconds)      
    print("repetition time is", rpt_time, "seconds")
  
    # List
    time_list=[]
    time_list.extend(seconds)
    print('Updated list:', time_list)


WRITE_n_SECONDS()