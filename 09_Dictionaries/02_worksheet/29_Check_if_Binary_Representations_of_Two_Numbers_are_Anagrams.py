'''
Given two numbers, check if their binary representations are anagrams (same bits, just shuffled).
Input: num1 = 5, num2 = 6
Expected Output: False
'''
num1 = 5
num2 = 5
if bin(num1) == bin(num2):
    print("True")
else:
    print("False")
    