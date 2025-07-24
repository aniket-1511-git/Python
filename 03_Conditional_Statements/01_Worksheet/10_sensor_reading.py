'''
Given three sensor readings, print "Majority High" if at least two readings are above a threshold (e.g., 50), otherwise "Majority Low".
Input: 40, 65, 70
Output: Majority High
'''
print("Enter sensor reading")
s1=int(input())
s2=int(input())
s3=int(input())

if s1>=50 :
    if s2>=50 or s3>=50:
        print( "Majority High")
    else: 
        print( "Majority Low")
elif s2>=50 :
    if s1>=50 or s3>=50:
        print( "Majority High")
    else: 
        print( "Majority Low")
elif s3>=50 :
    if s1>=50 or s2>=50:
        print( "Majority High")
    else: 
        print( "Majority Low")
else: 
    print( "Majority Low")