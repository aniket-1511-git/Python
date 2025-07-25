'''
Question: Write a function is_negative(number) that returns True if the number is negative, else False.
Sample data:
print(is_negative(-7))
print(is_negative(0))
Expected output:
True
False
'''
def isNeg(x:int):
    if x>0:
        return False
    else:
        return True
print("Enter no")
n=int(input())
print(isNeg(n))