'''
A nested dictionary holds employee info. An employee changed their phone number. Update it without touching the rest of their info.
Input: profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}, new_phone = '555-9999'
Expected Output: {'info': {'name': 'Sam', 'phone': '555-9999'}}
'''
profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}
new_phone = '555-9999'
profile['info']['phone']=new_phone
print(profile)

