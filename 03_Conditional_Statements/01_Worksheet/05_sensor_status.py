'''
If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
Input: 950
Output: Sensor Fault
'''
print("Enter voltage")
s=int(input())
if s>=100 and s<=900:
    print("Sensor OK")
else :
    print("Sensor Fault")
   