# Time manipulation 
from datetime import datetime
import pytz 

# current Datetime
unaware = datetime.now()
print('Timezone native:', unaware)

# Standard UTC timezone aware Datetime
aware = datetime.now(pytz.utc)
print('Timezone Aware:', aware)

dt_Rome = datetime.now(pytz.timezone('Europe/Rome'))
print("Europe Rome DateTime:", dt_Rome.strftime("%Y-%m-%d %H:%M:%S %Z %z"))

seconds = dt_Rome.strftime("%S")
print(seconds)
