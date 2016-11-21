
# coding: utf-8

# In[17]:

#Exercise 150:Removing comments

try:
    in_name = input("Enter the name of the python file:")
    file1 = open(in_name,"r")
except:
    print("Cannot open input file ")
    quit()

try:
    out_name = input("Enter the name of output file:")
    file2 = open(out_name,"w")
except:
    print("Cannot open output file ")
    quit()    

try:
    for line in file1:
        pos = line.find('#')
        
        if pos > -1:
            line = line[0:pos]
            line = line + "\n"
            
        file2.write(line)
        
    file1.close()
    file2.close()

except:
    print("Problem encountered while processing a file")
    quit()
    


# In[ ]:



