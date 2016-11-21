
# coding: utf-8

# In[ ]:

#Exercise 147:Words that occur most
import sys
file1 = open(sys.argv[1],"r")

lines = []
for line in file1:
    lines.append(line.split())
    lines = [val for sublist in lines for val in sublist]

lines = list(set(lines))
#lines = [c for c in lines if c not in ('!','.',':',',')]
#lines = [x.lower() for x in lines]
#freq_word = max(set(lines), key=lines.count)
print(lines)
#print("Word that occured most number of times is:%s"%freq_word)


# In[ ]:



