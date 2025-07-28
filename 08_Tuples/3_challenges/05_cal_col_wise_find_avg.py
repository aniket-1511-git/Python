'''
Description: Calculate the average of each column in a tuple of tuples and display the result as a list.
This is helpful for column-wise statistics and is frequently seen in spreadsheet-like computations.
Input: t = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Output: [30.5, 34.25, 27.0, 23.25]
'''
t = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
r= len(t)
c= len(t[0])
l=[]
print(r,c)
for i in range(0,r):
    s=0
    for j in range(0,c):
        s+=t[j][i]
    s=float(s//c)
    l.append(s)
print(l)