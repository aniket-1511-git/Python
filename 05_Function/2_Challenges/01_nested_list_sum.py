'''
Question: Write a function deep_sum(lst) that takes a nested list of integers (arbitrary levels of nesting) and returns the total sum of all integers.
Sample data:
deep_sum([1, [2, [3, 4], 5], 6])
Expected output:
21
'''
def nested_sum(l:list):
    s=0
    for i in l:
        if isinstance(i,list):
            s+=nested_sum(i)
        else:
            s+=i    
    return s
s=nested_sum([1, [2, [3, 4], 5], 6])
print("Sum ",s)