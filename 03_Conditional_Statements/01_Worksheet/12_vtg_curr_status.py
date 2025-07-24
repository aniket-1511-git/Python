'''
Given a voltage and current reading, print "Power OK" if both are in safe ranges, otherwise print specific error:
- Voltage out of 3.0–3.3V: "Voltage Error"
- Current out of 10–500mA: "Current Error"
- Both out: "Power Error"
'''
print("Enter current and voltage")
c=int(input())
v=float(input())
if v>3.3 and c >500:
    print("Power Error")
elif v>3.3:
    print("Voltage Error")
elif c>500:
    print("Current Error")
else:
    print("Power OK")
    
    
