'''
Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
Input: 18
Output: Low Temp
'''
print("Enter voltage")
temp=float(input())
if temp>75:
    print("Overheat")
elif temp>25:
    print("Normal")
else :
    print("Low Temp")
    