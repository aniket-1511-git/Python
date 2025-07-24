'''
For a given number, print its multiplication table from 1 to 10, but don’t use the * operator.
'''
print("Enter nu1")
n1=int(input())
print("Enter nu2")
n2=int(input())

for i in range(n1,n2):
    for j in range(1, 11):
        r = 0
        c = j
        while c > 0:
            r += i
            c -= 1
        print(str(i) + " x " + str(j) + " = " + str(r))
        