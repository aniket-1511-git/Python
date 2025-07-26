'''
Find Close Matches for a String in a List
Explanation: Find list entries that are similar to the given word (helpful for typo correction).
Input: Target = "apple", List = ["apply", "apples", "ape", "maple"]
Expected Output: Close matches: ['apply', 'apples']
'''
def isMatch(t:str,l:list):
    for i in l:
        if i.startswith(t) or t.startswith(i):
            print(i,end=" ")
l=["apply", "apples", "ape", "maple"]
t="apple"
isMatch(t,l)