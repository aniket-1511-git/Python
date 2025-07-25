'''
Question: Write a function min_max(numbers) that returns both the smallest and largest number in a list (use returning multiple values).
Sample data:
small, large = min_max([8, 3, 5, 2, 10])
print("Smallest:", small)
print("Largest:", large)
Expected output:
Smallest: 2
Largest: 10
'''
def max_min(l:list):
    max=l[0]
    min=l[0]
    for i in l:
        if max< i:
            max=i
        if min>i:
            min=i
    return min ,max
s,l=max_min([8, 3, 5, 2, 10])
print("Smallest: ",s)
print("Largest: ",l)