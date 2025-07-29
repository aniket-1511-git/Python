'''
Story: Pick a word from each basket to make a pair that covers all 26 letters!
Sample Input:
A = {"abc", "defg", "xyz"}
B = {"mnopq", "rstuv", "wxyz"}
Tip: Try making pairs and see if all alphabet letters are used together.
'''
import string
A = {"abc", "defg", "xyz"}
B = {"mnopq", "rstuv", "wxyz"}
all_letters = set(string.ascii_lowercase)
for a in A:
    for b in B:
        combined = set(a + b)
        if combined == all_letters:
            print(f"Pair found: ({a}, {b})")