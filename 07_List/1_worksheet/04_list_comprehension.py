'''
4. List Comprehension
Log Session a list of fruits: "apple", "banana", "cherry", "kiwi", "mango".
Use list comprehension to create a new list containing fruits with the letter "a".
Convert all fruit names to uppercase using list comprehension.
Replace "banana" with "orange" using list comprehension.
'''
l=["apple", "banana", "cherry", "kiwi", "mango"]
l1=[]
for i in l:
    if "a" in i:
        l1.append(i)
print(l1)
l1=[i.upper() for i in l1]
print(l1)
i=l1.index("BANANA")
l1[i]="orange"
print(l1)


