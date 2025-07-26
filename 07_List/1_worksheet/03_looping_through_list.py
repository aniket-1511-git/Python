'''
3. Looping Through Lists
Log Session a list of numbers from 1 to 5.
Use a for loop to print each number.
Use a while loop to print each number.
Use list comprehension to create a new list with each number squared.
'''
l=[1,2,3,4,5]
for i in l:
    print(i,end=" ")
i=0
print(" ")
while i<len(l):
    print(l[i],end=" ")
    i+=1
print(" ")
i=0
l1=[]
while i<len(l):
    l1.append(l[i]*l[i])
    i+=1
print(l1)


    