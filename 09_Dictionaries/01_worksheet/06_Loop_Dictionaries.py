'''
Iterating over dictionaries lets you process or filter keys and values.
Loop and print all keys in d = {'a': 10, 'b': 20, 'c': 30}.
Loop and print all values in the same dictionary.
Loop and print each key and its value together.
Print only the subjects with marks above 60 from scores = {'math': 75, 'science': 55, 'english': 82}.
Sample Output:
math
english
'''
d = {'a': 10, 'b': 20, 'c': 30}
for i in d:
    print(i,end=" ")
print(" ")
for i in d:
    print(d[i],end=" ")
print(" ")
for i in d:
    print(i,d[i])
scores = {'math': 75, 'science': 55, 'english': 82}
for i in scores:
    if scores[i]>=60:
        print(i)
print(" ")