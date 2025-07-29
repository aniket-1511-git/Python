'''
Story: You and your friend invent two words. Make a mashup with only letters not shared by both.
Sample Input:
word1 = "apple"
word2 = "orange"
Sample Output:
"plrgn"
Tip: What does set(word1) ^ set(word2) do?
'''
word1 = "apple"
word2 = "orange"
w12=str(set(word1)^set(word2))
print(w12)