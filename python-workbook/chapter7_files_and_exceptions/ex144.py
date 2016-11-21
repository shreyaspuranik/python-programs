
# coding: utf-8

# In[ ]:

#Exercise 144:Number lines in afile
import sys

file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
count = 1
for line in file1:
    file2.write (str(count)+':'+line)
    count+=1
file2.close()


