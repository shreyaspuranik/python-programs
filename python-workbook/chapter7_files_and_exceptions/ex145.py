

#Exercise 145:Find the Longest Word of File
import sys
file1 = open(sys.argv[1],"r")

lines = []
for line in file1:
    lines.append(line.split())
    lines = [val for sublist in lines for val in sublist]  #flattening a list

lines = list(set(lines))    #Remove duplicates
largestWord=""
words = []
for word in lines:       
    if len(largestWord)<len(word):
        largestWord= word
length = len(largestWord)
print("The longest word(s) in the list is %s and length is %d." %(largestWord,length))

file1.close()


