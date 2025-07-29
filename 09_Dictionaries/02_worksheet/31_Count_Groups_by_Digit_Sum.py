'''
Group numbers by the sum of their digits and report the size of the largest group.
Input: nums = [11, 20, 12, 21, 3]
Expected Output: 2
'''
def largest_digit_sum_group(nums):
    groups = {}
    for num in nums:
        digit_sum = sum(int(d) for d in str(num))
        groups[digit_sum] = groups.get(digit_sum, 0) +1
    return max(groups.values())

# Example input
nums = [11, 20, 12, 21, 3]
print(largest_digit_sum_group(nums))
