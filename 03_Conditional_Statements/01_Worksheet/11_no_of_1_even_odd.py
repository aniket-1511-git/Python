'''
Enter a 16-bit value and print if parity (number of 1s) is even or odd.
Input: 0xAAAA
Output: Parity: Even
'''
print("Enter no")
a=int(input())
c=bin(a).count('1')
print("Parity :", "Even" if c%2==0 else "Odd")