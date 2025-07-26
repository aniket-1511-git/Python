'''
Top 3 Most Frequent Error Keywords
Description: Given a kernel log string, count the most frequent error keywords: "fail", "error", "timeout", "panic" (case-insensitive). Show the top 3 with their counts.
Sample Input:
log = """
[1.11] ERROR: device failed to start
[1.12] ERROR: timeout waiting for response
[1.13] WARNING: low battery
[1.14] PANIC: unrecoverable error
[1.15] device fail detected
[1.16] timeout on bus
"""
Expected Output:
error: 3
fail: 2
timeout: 2
'''