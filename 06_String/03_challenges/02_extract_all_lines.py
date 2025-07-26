'''
Extract All Lines Containing WARNING With Timestamps
Description: From a multiline log string, print all lines that include the word "WARNING" (case-insensitive), including their timestamps.
Sample Input:
log = """
[100.123] INFO: Booting Linux
[100.456] WARNING: Low memory detected
[101.000] WARNING: CPU load high
[101.555] INFO: Boot complete
"""
Expected Output:
[100.456] WARNING: Low memory detected
[101.000] WARNING: CPU load high
'''
