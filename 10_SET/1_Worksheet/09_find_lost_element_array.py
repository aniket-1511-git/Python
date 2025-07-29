'''
Story: You had four marbles yesterday, now one is missing. Which one?
Sample Input:
yesterday = [1, 2, 3, 4]
today = [1, 4, 2]
Sample Output:
3
Tip: What does set(yesterday) - set(today) give you?
'''
yesterday = [1, 2, 3, 4]
today = [1, 4, 2]
print(list(set(yesterday) - set(today)))