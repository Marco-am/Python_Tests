import time
import pytz 
from datetime import datetime

def foo():
  print (time.ctime())

time_list=[]

while True:
  foo()
  rpt_time = 2.0
  time.sleep(rpt_time)

  dt_Rome = datetime.now(pytz.timezone('Europe/Rome'))
  print("(UTC-Europe Rome) DateTime:", dt_Rome.strftime("%Y-%m-%d %H:%M:%S %Z %z"))
  seconds = dt_Rome.strftime("%S") 
  print("repetition time is", rpt_time, "seconds", "actual second counter:",seconds,"\n")  

  # List  
  list_length = len(time_list)  
  time_list.append(seconds)   
  print('List legth:', list_length) 
  print(time_list)  

