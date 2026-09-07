





#Block 1
def afficher_message(message):
    print(message)
def diviser_avec_reste(a,b):
    return (a//b,a%b)
#Bolck2
def somme(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
def construire_fiche(**infos):
    print('*'*4,end='')
    print('Fiche D\'information',end='')
    print('*'*4)
    for k,v in infos.items():
        print(f'{k}: {v}')

def addition(a:int, b:int)->int:
    return a+b
#Block3
counter = 0
def inc_local():
    global  counter
    counter = counter + 1
    return counter
def cree_counter():
    value = 0
    def incrementer():
        nonlocal value
        value = value + 1
        return value
    return incrementer
def mult(a,b):
    return a*b
def apply_operation(a,b,operation):
    return operation(a,b)
#Python Closures
def creer_multiplicateur(facteur):
    def remember(y):
        return facteur*y
    return remember

def main():
    #Block 1
    resultat = afficher_message("Traitement termine")
    print(resultat)

    quotient, reste = diviser_avec_reste(17, 5)
    print('quotient = ',quotient,'reste = ',reste)
    #Bolck2
    print('sum of 1,2 and 3 is: ',somme(1,2,3))
    print('sum of 55 and 3 is: ',somme(55,3))
    print('sum with no args: ',somme())

    construire_fiche(nom="Ali", age=25, ville="Casablanca")

    print(addition(2, 3))
    print(addition(2.5, 3.5))
    #Block3
    inc_local()
    inc_local()
    inc_local()
    inc_local()
    print('incresement: ',inc_local())

    counter1 = cree_counter()
    counter1()
    counter1()
    counter1()
    print('COUNTER 1: ',counter1())

    print('add: ',apply_operation(4,5,addition))
    print('mult: ',apply_operation(4,5,mult))

    fois_trois = creer_multiplicateur(3)
    fois_dix = creer_multiplicateur(10)
    print(fois_trois(7))
    print(fois_dix(7))

main()