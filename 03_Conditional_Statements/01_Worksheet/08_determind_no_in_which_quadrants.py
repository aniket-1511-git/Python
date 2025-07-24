'''
Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
- 0–63, 64–127, 128–191, 192–255
'''
print("Enter no")
a=int(input())
if a>=192 and a<=255:
    print("4th quadrant")
elif a>=128 and a<=191:
    print("3rd quadrant")
elif a>=64 and a<= 127:
    print("2nd quadrant")
elif a>=63 and a<= 0:
    print("1st quadrant")
