def calc_mean(notes):
    sum = 0
    n = 0
    for note in notes:
        sum = sum + note
        n = n + 1
    mean = sum / n
    return mean
def appreciation(mean):
    if(mean < 10 ): return 'Insuffisant'
    elif(mean >= 10 and mean < 12 ): return  'Passable'
    elif(mean >=12 and mean < 16 ): return  'Bien'
    elif(mean >=16 and mean <= 20 ): return  'Tres Bien'

students = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
]
resultats = {}
for student in students:
    mean = calc_mean(student['notes'])
    resultats[student['nom']] = {
        'moyenne': round(mean,2),
        'mention':appreciation(mean)
    }

sorted_students = sorted(resultats.items(),key=lambda student:student[1]['moyenne'],reverse=True)
print(resultats)

for i,student in enumerate(sorted_students):
    print(f'{i+1}. {student[0]} - {student[1]['moyenne']}')

def students_expected_to_fail(students):
    return [(student[0],student[1]['moyenne']) for student in students.items() if student[1]['moyenne'] < 10]

print('students expected to fail',students_expected_to_fail(resultats))