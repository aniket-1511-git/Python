'''
Task: Write a Python function to find the maximum sum sub-sequence in a list (sub-sequence, not necessarily contiguous).
Sample input: [2, -1, 2, 3, 4, -5]
Output: 11
(The maximum sum subsequence is 2 + 2 + 3 + 4)
'''
l1=[2, -1, 2, 3, 4, -5]
m = 0
for num in l1:
    if num > 0:
        m += num
print(m)
    
