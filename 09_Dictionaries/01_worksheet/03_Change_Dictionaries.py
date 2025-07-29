'''
Updating dictionary values is needed when data changes during runtime.
Update the age of 'Anil' from 21 to 22 in this dictionary: ages = {'Anil': 21, 'Sunita': 20}.
Change multiple values at once in the dictionary: info = {'a': 10, 'b': 20} so that both 'a' and 'b' become 100.
Increase every salary in salaries = {'A': 20000, 'B': 30000} by 10%.
Sample Output: {'A': 22000.0, 'B': 33000.0}
Assign a value to a key that doesn't exist (e.g., add 'C': 25000 to salaries). What happens?
'''
ages = {'Anil': 21, 'Sunita': 20}
print(ages)
ages['Anil']=22
print(ages)
info = {'a': 10, 'b': 20}
print(info)
for i in info:
    info[i]=100
print(info)
sal = {'A': 20000, 'B': 30000}
print(sal)
for i in sal:
    s=sal[i]//10
    sal[i]+=s
print(sal)
sal.update({'C':25000})
print(sal)