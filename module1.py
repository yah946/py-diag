

def readNoteBetween(n1,n2):
    note = 9999
    while (note < n1 or note > n2):
        note = float(input('Enter a note: '))
        if(note < n1 or note > n2): print(f'enter a note between {n1} and {n2}, try agian!')
    return float(note)

def calc_mean(notes):
    sum = 0
    n = 0
    for note in notes:
        sum = sum + note
        n = n + 1
    mean = sum / n
    return mean
def appreciation(means):
    app = ''
    for mean in means:
        if(mean < 10 ): app = 'Insuffisant'
        elif(mean >= 10 and mean < 12 ): app =  'Passable'
        elif(mean >=12 and mean < 16 ): app =  'Bien'
        elif(mean >=16 and mean <= 20 ): app =  'Tres Bien'
        print(f'{mean} -> {app}')

def main():
    students = []

    student = {'first_name':'Unknown','last_name':'Unknown','notes':[]}

    student['first_name'] = input("Enter Your First Name: ")
    student['last_name'] = input("Enter Your Last Name: ")
    a = readNoteBetween(1,20)
    b = readNoteBetween(1,20)
    c = readNoteBetween(1,20)
    student['notes'].extend([a,b,c])
    
    mean = calc_mean(student['notes'])
    appreciation( [9.9, 10.0, 11.9, 12.0, 15.9, 16.0, 20.0])

    print(f'{student["first_name"]} mean: {mean:>6.2f}')

main()