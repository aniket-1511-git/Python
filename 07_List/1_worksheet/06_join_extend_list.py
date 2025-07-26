'''
6. Joining and Extending Lists
Log Session two lists: list1 = ["a", "b", "c"] and list2 = [1, 2, 3].
Concatenate the two lists into a new list.
Use the extend() method to add list2 to list1.
Print the final lists.
'''
l1 = ["a", "b", "c"] 
l2 = [1, 2, 3]
l3=[]
i=0
while i<len(l1):
    l3.append(l1[i])
    i+=1
i=0
while i<len(l2):
    l3.append(l2[i])
    i+=1
print(l3)
l2.extend(l1)
print(l2)
