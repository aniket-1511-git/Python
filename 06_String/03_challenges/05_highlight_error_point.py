''''
Highlight All Error Lines and Show Context
Description: For each line containing "error" (case-insensitive), print that line plus the previous and next line for context.
Sample Input:
log = """
[10.00] Starting system
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended
"""
Expected Output:
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device

[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended
'''