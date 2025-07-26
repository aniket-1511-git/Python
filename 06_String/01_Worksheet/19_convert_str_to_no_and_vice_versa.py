'''
Convert Integer to String and Vice Versa
Explanation: Change a number to a string, and a string of digits to an integer.
Input: Integer = 123, String = "456"
Expected Output:
Integer to string: '123'
String to integer: 456
'''
def covertion(s1:str,n:int):
    s=str(n)
    i=int(s1)    
    return i,s
i, s =covertion("456",123)
print("int ",i)
print("string ",s)
        
    