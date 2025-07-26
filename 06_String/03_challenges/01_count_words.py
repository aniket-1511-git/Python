'''
Count Number of Kernel Panics and Oops
Description: Given a string containing kernel logs, count how many times "kernel panic" and "Oops" appear (case-insensitive).
Sample Input:
log = """
[12345.67] kernel panic - not syncing: Fatal exception
[12345.89] Oops: 0002 [#1] SMP
[12346.00] kernel panic - not syncing: Fatal exception
[12346.13] Oops: 0003 [#2] SMP
"""
Expected Output:
Kernel panic count: 2
Oops count: 2''
'''
