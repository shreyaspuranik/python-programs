
# coding: utf-8

# In[ ]:

#Exercise 143:Concatenate Multiple files
import sys
if len(sys.argv) == 1:
    print("Atleast one file name must be given")
    quit()
    
for i in range(1,len(sys.argv)):
    fname = sys.argv[i]
    try:
        file1 = open(fname,"r")
        
        for line in file1:
            print(line,end = "")
            
        file1.close()
        
    except:
        print("Couldn't open",fname)
        

