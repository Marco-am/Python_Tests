# Asincronous programming, simulated event triggered interrupt - MDS 2022  
import signal
import sys
import time

global keeponline
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    print ("Keeponline is"), keeponline
    print ("Saving the value")
    
    fd = open("output.txt","w+")
    fd.write(str(keeponline))
    fd.close()

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#Initilization
keeponline = 0

# Create a File heading  
First_doc_lines = ['#Test file', 'How to write something inside .txt file']
# 'w'	Open a text file for writing text     'a'   Open a text file for appending text
with open('Marco_Test_File.txt', 'w') as TexFile_handler_Marco:
    for line in First_doc_lines:
        TexFile_handler_Marco.write(line)
        TexFile_handler_Marco.write('\n')

#Read a line in the file every second and increment the variable
fd = open("Marco_Test_File.txt","r")

while True:
    line = fd.readline()
    keeponline += 1

    print ("Line:"), line
    time.sleep(2)

    #It is just an example condition
    if ( len(line) == 0 ):
        break

fd.close()