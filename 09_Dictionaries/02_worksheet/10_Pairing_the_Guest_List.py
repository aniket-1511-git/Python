'''
You have two lists: guest names and their seat numbers. Match each guest to their seat for the dinner plan!
Input: names = ['Alice', 'Bob', 'Eve'], seats = [5, 12, 8]
Expected Output: {'Alice': 5, 'Bob': 12, 'Eve': 8}
'''
names = ['Alice', 'Bob', 'Eve']
seats = [5, 12, 8]
d=dict(zip(names,seats))
print(d)
