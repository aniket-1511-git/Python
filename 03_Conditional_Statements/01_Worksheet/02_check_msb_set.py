'''
Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
Input: 0b10010010
Output: MSB set
'''
print("Enter no")
a=int(input())
print(bin(a))

for i in range(7,0,-1):
    if a>>i&1:
        print("MSB set")
        break

