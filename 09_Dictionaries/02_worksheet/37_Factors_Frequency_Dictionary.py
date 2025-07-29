'''
Count the frequency of each factor for all numbers in a list using a dictionary.
Input: nums = [10, 15]
Expected Output: {1: 2, 2: 1, 5: 2, 10: 1, 3: 1, 15: 1}
'''
from collections import defaultdict
nums = [10, 15]
freq = defaultdict(int)

for num in nums:
    for i in range(1, num + 1):
        if num % i == 0:
            freq[i] += 1

result = dict(freq)
print(result)