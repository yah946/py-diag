


def read_file_safely(path):
    try:
        with open(path,'r',encoding='utf-8') as f:
            lsContent = f.readlines()
            return lsContent
    except FileNotFoundError as e:
        print(f'Error: The file "{path}" does not exist.')
def calculate_average_csv(path):
    lines = read_file_safely(path)
    notes = []
    #remove names and guard notes
    for i in range(1,len(lines)):
        try:
            name = lines[i].split(',')[0]
            note = lines[i].split(',')[1][:-1]
            num = int(note)
        except ValueError:
            print(f'Warning: Invalid note for "{name}" ("{note}"), line ignored.')
        else:
            notes.append(num)
    mean = sum(notes) / len(notes)
    return round(mean,2)

def main():
    # print(read_file_safely("courses.txt"))
    # read_file_safely("nonexistent.txt")

    print('Calculated average: ',calculate_average_csv("notes.csv"))



main()