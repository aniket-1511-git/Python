'''
Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000–9999), "High Band" (10000–99999), or "Out of Range".
Input: 8000
Output: Mid Band
'''
print("Enter Freq")
freq=int(input())
if freq<1000:
    print("Low Band")
elif freq<=9999 and freq>=1000:
    print("Mid Band")
elif freq<=99999 and freq>=10000:
    print("High Band")
elif freq>99999:
    print("Out of Band")
    
    
    