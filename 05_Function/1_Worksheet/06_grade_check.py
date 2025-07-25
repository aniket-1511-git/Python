'''
Question: Write a function grade(score) that returns 'A' if score ≥ 90, 'B' if 80 ≤ score < 90, 'C' if 70 ≤ score < 80, and 'F' for anything less.
Sample data:
print(grade(85))
print(grade(72))
print(grade(50))
Expected output:
B
C
F
'''
def grade(x:int):
    if x>=90:
        return 'A'
    elif x>=80:
        return 'B'
    elif x>=70:
        return 'C'
    else:
        return 'F'
print("Enter mrks")
n=int(input())
print(grade(n))
    
        