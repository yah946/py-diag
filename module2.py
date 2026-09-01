

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

def main():
    students = [
        {"nom": "Karim", "notes": [12, 15, 9]},
        {"nom": "Sara", "notes": [18, 17, 16]},
        {"nom": "Lina", "notes": [6, 8, 5]},
    ]
    for student in students:
        mean = calc_mean(student['notes'])
        student['mean'] = mean
        print(f'{student['nom']} {mean} {appreciation(mean)}')
    students_sorted = sorted(students,key = lambda d: d[mean])
    print (students_sorted)


main()