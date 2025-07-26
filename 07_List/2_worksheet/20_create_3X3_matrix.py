'''
Task: Write a Python program to create a 3x3 matrix using nested list comprehensions.
Sample input: Rows: 3, Columns: 3
Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
'''
print("Enter row and col")
r=int(input())
c=int(input())
m=[]
for i in range(0,r):
   m.append([]) 
   for j in range (0,c):
       m[i].append(i)
       j+=1
   i+=1
print(m)
    