'''
Write a Python function that uses a regular expression to extract all unique IPv4 addresses
from the log file. Some log messages include IP addresses (e.g., “Ping to server
192.168.1.100 succeeded”). Return a list of unique IP addresses found.
Challenge: Ensure your regex correctly matches typical IPv4 formats and does not capture
invalid patterns.
'''

import re

def extract_unique_ipv4_addresses(log_file_path):
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    found_ips = set()

    with open(log_file_path, 'r') as file:
        for line in file:
            matches = re.findall(ipv4_pattern, line)
            for ip in matches:
                octets = ip.split('.')
                if all(0 <= int(o) <= 255 for o in octets):
                    found_ips.add(ip)

    return sorted(found_ips)

log_file = "data_log.txt"
ip_list = extract_unique_ipv4_addresses(log_file)
print("\nUnique IPv4 Addresses Found:")
for ip in ip_list:
        print(ip)
