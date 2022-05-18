# Asincronous programming, simulated interrupt event - MDS 2022  
import signal
import sys
import time

global Keep_line
def signal_handler(signal, frame):
    print ('You pressed Ctrl+C!')
    print ("Keep_line is:", Keep_line)
    print ("Saving the value")
    
    f_Handl_MDS = open("output.txt","w+")
    f_Handl_MDS.write(str(Keep_line))
    f_Handl_MDS.close()

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#Initilization
Keep_line = " Nothing to read from file "

# Create the File heading  
First_doc_lines = ['#Test file', 'How to write something inside .txt file', 'row 3', 'row 4', 'row 5']
# 'w' Open a text file for writing text        'a' Open a text file for appending text
with open('Marco_Test_File.txt', 'w') as TexFile_handler_Marco:
    for line in First_doc_lines:
        TexFile_handler_Marco.write(line)
        TexFile_handler_Marco.write('\n')


# open file 
TexFile_handler_Marco = open("Marco_Test_File.txt","r")

while True:
    # print time every 'rpt_time' and sleep for 'rpt_time' 
    print (time.ctime())
    rpt_time = 2.0
    time.sleep(rpt_time)
    #Read a line in the file every second
    line = TexFile_handler_Marco.readline()
    Keep_line = line 
    # # example of Exit condition
    # if ( len(line) == 0 ):
    #     break

# close file 
TexFile_handler_Marco.close()