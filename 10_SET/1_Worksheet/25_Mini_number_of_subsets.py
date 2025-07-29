'''
Story: You have lots of marbles. How many bags do you need so that no bag has two marbles of the same color?
Sample Input:
marbles = ["red", "blue", "red", "green", "blue", "red"]
Sample Output:
3
Tip: The most common color
'''
marbles = ["red", "blue", "red", "green", "blue", "red"]
c = max(marbles)
print(c)