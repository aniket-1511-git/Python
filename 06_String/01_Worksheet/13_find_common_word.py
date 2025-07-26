'''
Find Uncommon Words Between Two Strings
Explanation: List words present in only one of the two strings.
Input: "red blue green", "blue yellow red"
Expected Output: Uncommon words: ['green', 'yellow']
'''
from collections import Counter
def findComWord(s1:str, s2:str):
    w1 = s1.split()
    w2 = s2.split()
    all_words = w1 + w2
    word_count = Counter(all_words)
    uncommon = [word for word in word_count if word_count[word] == 1]
    return uncommon
s1 = "red blue green"
s2 = "blue yellow red"
result = findComWord(s1, s2)
print("Uncommon words:", result)
