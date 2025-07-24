'''
Given two pin logic levels (0 or 1), print the type of logic gate output if these were inputs to an AND, OR, and XOR gate.
Input: 1, 0
Output: AND: 0, OR: 1, XOR: 1
'''
print("Enter no1")
a=int(input())
print("Enter no2")
b=int(input())
    # AND gate
    
if a and b:
    print("AND : 1")
else :
    print("AND : 0")
    
    # OR Gate 
    
if (a and b) or a or b:
    print("OR : 1")
else :
    print("OR : 0")
    
    # XOR Gate 
    
if (a==0 and b) or (a and b==0):
    print("XOR : 1")
else :
    print("XOR : 0")
    
    
        
    
