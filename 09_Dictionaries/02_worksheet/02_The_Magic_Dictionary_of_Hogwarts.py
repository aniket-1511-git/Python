'''
2. The Magic Dictionary of Hogwarts
Every student at Hogwarts has a pet. Sometimes, a student forgets to register a pet. If someone asks for Hermione’s pet, and her name isn’t registered, you must politely tell them “No record, maybe try another student!” Can you build this polite pet query?
Input: pets = {'Harry': 'owl', 'Ron': 'rat'}, query = 'Hermione'
Expected Output: No record, maybe try another student!
'''
pets = {'Harry': 'owl', 'Ron': 'rat'}
p= pets.get('Hermione')
if p== None:
    print(" No record")
else:
    print(" Yes ")
