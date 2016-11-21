
# coding: utf-8

# In[1]:

#Exercise 141:Display Head of file
import sys


if len(sys.argv) !=2:
    print("File name not given")
    quit()

try:
    file1 = open(sys.argv[1],"r")
    line = file1.readline()
    
    count = 0
    while count < 10 and line != "":
        line = line.rstrip()
        count = count + 1
        
        print(line)
        line = file1.readline()
        
    file1.close()
    
except IOError:
    print("Cannot access file")
        


# In[ ]:



