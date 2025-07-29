'''
Build a scoring matrix for students and subjects using a dictionary.
Input: students = ['A', 'B'], subjects = ['math', 'sci'], scores = [[90, 80], [85, 95]]
Expected Output: {'A': {'math': 90, 'sci': 80}, 'B': {'math': 85, 'sci': 95}}
'''
students = ['A', 'B']
subjects = ['math', 'sci']
scores = [[90, 80], [85, 95]]

result = {
    student: {subject: score for subject, score in zip(subjects, row)}
    for student, row in zip(students, scores)
}
print(result)