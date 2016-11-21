
# coding: utf-8

# In[ ]:

#Exercise 151:Two word random password
from random import randrange
word_file = "passwords.txt"

words = []
file1 = open(word_file,"r")
for line in file1:
    line = line.rstrip()
    
    if len(line) >= 3 and len(line) <= 7:
        words.append(line)
        
file1.close()

first = words[randrange(0,len(words))]
first = first.capitalize()

password = first
while len(password) < 8 or len(password) > 10:
    second = words[randrange(0,len(words))]
    second = second.capitalize()
    password = first + second
    
print("The random password is:",password)
         
        
    



# In[ ]:



