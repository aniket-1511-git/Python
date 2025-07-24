'''
Take an integer input and print its digits in reverse order (don’t use slicing or strings).
'''
print("Enter nu")
n=int(input())
r=0
while n>0:
    r=r*10+(n%10)
    n//=10
print("reverse no :",r)