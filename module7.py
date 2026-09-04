
def total_per_product(sales):
    total = {}
    for sale in sales:
        if sale['produit'] in total:
            total[sale['produit']] += sale['montant']
        else:
            total[sale['produit']] = sale['montant']
    return total
#{'pommes': 165, 'bananes': 110, 'oranges': 60}
def merge_inventories(inv1,inv2): 
    merge = {}
    for item in inv1:
        if item in merge:
            merge[item] += inv1[item]
        else:
            merge[item] = inv1[item]
    for item in inv2:
       if item in merge:
            merge[item] += inv2[item]
       else:
            merge[item] = inv2[item]
    return merge
def print_mean_of_each_student(students):
    for student in students:
        notes = []
        for note in student['matieres'].values():
            notes.append(note)
        mean = sum(notes)/len(notes)
        print(f'{student['nom']}: {mean:.2f}')
def all_school_subject(students):
    subjects = set()
    for student in students:
        for subject in student['matieres']:
            subjects.add(subject)
    return subjects
def grades_per_subject(students):
    subjects = {}
    for student in students:
        for subject in student['matieres']:
            if subject in subjects:
                subjects[subject].append(student['matieres'][subject])
            else:
                subjects[subject] = []
                subjects[subject].append(student['matieres'][subject])
    return subjects
def main():
    sales = [
        {"produit": "pommes", "montant": 120},
        {"produit": "bananes", "montant": 80},
        {"produit": "pommes", "montant": 45},
        {"produit": "oranges", "montant": 60},
        {"produit": "bananes", "montant": 30},
    ]
    inv1 = {"pommes": 20, "bananes": 15}
    inv2 = {"bananes": 10, "kiwis": 5}
    students = [
        {"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
        {"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
        {"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
    ]


    # total = total_per_product(sales)
    # print("Total par produit : ",total)
    # maxi = max(total,key=lambda x: total[x])

    # print(f"Meilleur produit  : {maxi} ({total[maxi]})")
    # print("Produits distincts: ",set(total))

    # print(merge_inventories(inv1,inv2))

    # print('Moyenne par etudiant:')
    # print_mean_of_each_student(students)
    # print('Matieres enseignees (set): ',all_school_subject(students))
    # print('Notes par matiere: ')
    grades_per_subject_dic = grades_per_subject(students)
    # for k,v in grades_per_subject_dic.items():
    #     print(f'{k}: {v}')
    # for subject,notes_list in grades_per_subject_dic.items():
    max(grades_per_subject_dic.items(), key=lambda x: sum(x[1]) / len(x[1]))
    subject_best_mean = max(grades_per_subject_dic.items(), key=lambda x: sum(x[1]) / len(x[1]))
    print(f'Meilleure matiere (moyenne globale) : {subject_best_mean[0]} ({subject_best_mean[1][0]})')


main()