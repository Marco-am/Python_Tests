# Asincronous programming, simulated interrupt event - MDS 2022  
import signal
import sys
import time

global Keep_line
def signal_handler(signal, frame):
    print ('You pressed Ctrl+C!')
    print ("Program will stop")
    
    f_Handl_MDS = open("output.txt","w+")
    f_Handl_MDS.write(" Stopped from Asyncronous interrupt ")
    f_Handl_MDS.close()

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Write something inside the txt file  
Doc_lines = ['#Test file', 'How to write something inside .txt file', 'row 3', 'row 4', 'row 5']
# 'w' Open a text file for writing text  
with open('Marco_Test_File.txt', 'w') as TexFile_handler_Marco:
    for line in Doc_lines:
        TexFile_handler_Marco.write(line)
        TexFile_handler_Marco.write('\n')

while True:
    # print time value every 'rpt_time' and sleep for 'rpt_time' 
    print (time.ctime())
    rpt_time = 2.0
    time.sleep(rpt_time)