
# coding: utf-8

# In[2]:

#Exercise 142:Display the tail of a file
import sys 

if len(sys.argv) !=2:
    print("File name not given")
    quit()

try:
    file1 = open(sys.argv[1],"r")
    
    lines = []
    for line in file1:
        lines.append(line)
        if len(lines) > 10:
            lines.pop(0)
            
    file1.close()

except:
    print("Cannot access file")
    quit()
    
for line in lines:
    print(line,end = "")
    
        


# In[ ]:



