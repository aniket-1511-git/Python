'''
Count all distinct substrings of a string using Rabin-Karp algorithm and a dictionary.
Input: s = "abc"
Expected Output: 6
'''
def count_distinct_substrings(s):
    base = 256
    mod = 10**9 + 7
    n = len(s)
    seen = set()

    for length in range(1, n + 1):
        hash_val = 0
        power = 1
        for i in range(length):
            hash_val = (hash_val * base + ord(s[i])) % mod
            if i < length - 1:
                power = (power * base) % mod
        seen.add(hash_val)

        for i in range(1, n - length + 1):
            hash_val = (hash_val - ord(s[i - 1]) * power) % mod
            hash_val = (hash_val * base + ord(s[i + length - 1])) % mod
            seen.add(hash_val)

    return len(seen)

s = "abc"
print( count_distinct_substrings(s))  # Output: 6
