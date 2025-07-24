'''
Accept a device mode value:
- 0: "Standby"
- 1: "Active"
- 2: "Fault"
- Any other: "Unknown mode"
'''
print("Enter Device status")
stat=int(input())
if stat ==0:
    print("Standby")
elif stat ==1:
    print("Active")
elif stat ==2:
    print("Fault")
else:
    print("Unknown mode")