'''
 Concepts: 
 Variables, basic data types (integers, floats, strings), and control structures (ifelse, loops). 
 Task:  
 Write a script that reads a text file and counts the occurrence of each word. 
 Validation: 
 Verify that the output dictionary correctly represents word counts for given test files. 
 '''
from collections import defaultdict


fd = open ('data01.txt','r')
s=fd.read()
l=s.split()
d= defaultdict(int)
for i in l:
    d[i]+=1
print(d)