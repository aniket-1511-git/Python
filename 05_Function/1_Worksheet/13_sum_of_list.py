'''
Question: Write a recursive function sum_list(lst) to return the sum of all elements in a list.
Sample data:
print(sum_list([1, 2, 3, 4]))
Expected output:
10
'''
def list_sum(l:list):
    s=0
    for i in l:
        s+=i
    return s
print("Sum : ",list_sum([1,2,3,4,5]))