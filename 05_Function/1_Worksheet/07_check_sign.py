'''
Question: Write a function sign(num) that returns 'Positive' if num > 0, 'Negative' if num < 0, and 'Zero' if num == 0.
Sample data:
print(sign(10))
print(sign(-4))
print(sign(0))
Expected output:
Positive
Negative
Zero
'''
def numSign(a:int):
    if a>0:
        return "Positive"
    elif a<0:
        return "Negative"
    else:
        return "Zero"
print("Enter mrks")
n=int(input())
print(numSign(n))