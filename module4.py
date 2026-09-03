def min(items):
    minimum = items[0]
    for item in items:
        if(item<minimum): minimum = item
    return minimum

def max(items):
    maximum = items[0]
    for item in items:
        if(item>maximum): maximum = item
    return maximum

def filter(items,threshold):
    filtered_list = []
    for item in items:
        if item > threshold: filtered_list.append(item)
    return filtered_list
def occurrence_counting(items):
    occurrences = {}
    for item in items:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences
def print_dic_items(dictionary):
    for key,value in dictionary.items():
        print(f"{key}: {value}")
def occurrence_counting_tuple_version(items):
    occ = ()
    for item in items:
        trouve = False
        for ele in occ:
            if item == ele[0]:
                ele[1][0] += 1
                trouve = True
                break
        if not trouve:
            occ = occ + ((item,[1]),)
    return occ
def print_tuple_elements(occ):
    for ele in occ:
        print(f"{ele[0]}: {ele[1][0]}")
def reverse(items):
    reversed_list = []
    for i in range(len(items)-1,-1,-1):
        reversed_list.append(items[i]) 
    return reversed_list   
def merge(list_a,list_b):
    merged_list = list_a + list_b
    return sorte(merged_list,False)

def sorte(shuffle_numbers,acs = True):
    if acs:
        for i in range(len(shuffle_numbers)):
            for j in range(len(shuffle_numbers)):
                if shuffle_numbers[i] > shuffle_numbers[j]:
                    shuffle_numbers[i],shuffle_numbers[j] = shuffle_numbers[j],shuffle_numbers[i]
    else:
        for i in range(len(shuffle_numbers)):
            for j in range(len(shuffle_numbers)):
                if shuffle_numbers[i] < shuffle_numbers[j]:
                    shuffle_numbers[i],shuffle_numbers[j] = shuffle_numbers[j],shuffle_numbers[i]
    return shuffle_numbers
...

def main():

    notes = [12, 18, 7, 15, 9, 20, 3, 14]
    threshold = 12
    fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
    list_a = [1, 4, 7]
    list_b = [2,3,8,9]

    # print("Max Number",max(notes))
    # print("Min Number",min(notes))
    # print(filter(notes,threshold))

    # print("***Dic Version***")
    # print_dic_items(occurrence_counting(fruits))
    # print("***Tuple Version***")
    # print_tuple_elements(occurrence_counting_tuple_version(fruits))

    # print(reverse(notes))

    # print(merge(list_a,list_b))

    print([note**2 for note in notes if note%2==0])

main()