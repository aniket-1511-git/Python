'''
Given the status of three LEDs (on/off as 1/0), print which LEDs are ON. If all are off, print "All LEDs off".
Input: 0, 1, 0
Output: LED2 ON
'''
print("Enter LED status")
l1=int(input())
l2=int(input())
l3=int(input())

if l1 and l2 and l3 :
    print("All LEDs On")
elif l1 and l2==0 and l3==0 :
    print("LED1 ON")
elif l1==0 and l2 and l3==0 :
    print("LED2 ON")
elif l1==0 and l2==0 and l3 :
    print("LED3 ON")
elif l1 and l2 and l3==0 :
    print("LED1 & LED2 ON")
elif l1 and l2 ==0  and l3:
    print("LED1 & LED3 ON")
elif l1 and l2 and l3==0 :
    print("LED1 & LED2 ON")
elif l1 ==0 and l2   and l3:
    print("LED2 & LED3 ON")
else :
    print("All LEDs off")
    