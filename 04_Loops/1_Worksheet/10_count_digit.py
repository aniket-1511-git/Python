'''
Input a number and count how many digits it contains, using only arithmetic and loops.
'''
print("Enter nu")
n=int(input())
c=0
while n:
    c+=1
    n//=10
print("No of Digits ",c) 