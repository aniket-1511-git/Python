'''
Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
- "System Safe" if only `power_on` is True.
- "Shut Down: Overcurrent" if `overcurrent` is True.
- "Shut Down: Overvoltage" if `overvoltage` is True.
- "Critical Failure" if both faults are True.
Input: True, True, False
Output: Shut Down: Overcurrent
'''
print("Enter Flag status")
power_on=int(input())
overcurrent=int(input())
overvoltage=int(input())
print(power_on,overcurrent,overvoltage)
if overvoltage and overcurrent and power_on:
    print("Critical Failure")
elif power_on and overcurrent:
    print("Shut Down: Overcurrent")
elif power_on and overvoltage:
    print("Shut Down: Overvoltage")
elif power_on:
    print("System Safe")
