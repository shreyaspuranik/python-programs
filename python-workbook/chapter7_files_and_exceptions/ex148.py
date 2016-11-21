
# coding: utf-8

# In[17]:

#Exercise 148:Sum a List of Numbers
line = input("Enter a number:")
total = 0

while line != "":
    try:
        num = float(line)
        total = total + num
        
    except ValueError:
        print("Not a number")
    
    line = input("Enter a number:")

print("The grand total is %.2f"%total)


# In[ ]:



