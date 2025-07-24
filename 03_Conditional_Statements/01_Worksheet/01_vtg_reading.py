'''
Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
(Nominal is between 3.0V and 3.3V inclusive.)
Input: 3.35
'''
print("Enter voltage")
vtg=float(input())
if vtg>3.3:
    print("Over Voltage")
elif vtg>=3.0 and vtg<=3.3:
    print("Nominal Voltage")
else :
    print("Under Voltage")
    