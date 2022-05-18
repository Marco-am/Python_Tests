import keyboard

First_doc_lines = ['#Test file', 'How to write something inside .txt file']
# 'w'	Open a text file for writing text
# 'a'   Open a text file for appending text
with open('Marco_Test_File.txt', 'w') as f:
    for line in First_doc_lines:
        f.write(line)
        f.write('\n')

input("Press Enter to continue...")        