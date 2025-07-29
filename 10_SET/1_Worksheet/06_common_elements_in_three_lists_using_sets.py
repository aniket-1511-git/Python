'''
Story: Three friends want to pick a movie everyone likes. Which ones do they all like?
Sample Input:
a = ["Toy Story", "Frozen", "Moana"]
b = ["Moana", "Coco", "Frozen"]
c = ["Frozen", "Moana", "Up"]
Sample Output:
["Frozen", "Moana"]
Tip: Can you use set.intersection for this?
'''
a = ["Toy Story", "Frozen", "Moana"]
b = ["Moana", "Coco", "Frozen"]
c = ["Frozen", "Moana", "Up"]
a=set(a)
b=set(b)
c=set(c)
l=a.intersection(b,c)
print(l)
# for i in a:
#     if i in b and i in c:
#         print(i,end=" ")
