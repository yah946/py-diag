





def division_securisee(a, b):
    result = None
    try:
        result = a/b
    except ZeroDivisionError:
        print('Erreur : division par zero impossible.')
    except TypeError:
        print("String Entred")
    return result
def convertir_entier(valeur):
    result = None
    try:
        result = int(valeur)
    except ValueError:
        print(f'Erreur : "{valeur}" n\'est pas un entier valide.')
    return result
def acceder_element(liste, index):
    try:
        return liste[index]
    except IndexError:
        print(f'Erreur : index {index} hors limites (taille de la liste : {len(liste)}).')
def acceder_cle(dictionnaire, cle):
    try:
        return dictionnaire[cle]
    except KeyError:
        print(f'Erreur : la cle "{cle}" n\'existe pas.')
def traiter_valeur(value):
    result = None
    try:
        result = int(value)
    except ValueError:
        print(f'Erreur : "{value}" n\'est pas convertible.')
    else:
        print(f'Conversion reussie : {value}')
    finally:
        print('Traitement termine.')
def main():
    # Erreur de syntaxe ou exception
    extrait_a = "print('bonjour'" #SyntaxError: patenthese non fermee
    extrait_b = "resultat = 10 / 0" #ZeroDivsionError: exception a l'execution
    extrait_c = "valeurs = [1, 2, 3]\nprint(valeurs[5])" #IndexError: exception a l'execution

    print(division_securisee(10, 2))
    print(division_securisee(10, 0))
    print(division_securisee("i", 0))

    print(convertir_entier("42"))
    print(convertir_entier("abc"))

    notes = [12, 15, 9]
    print(acceder_element(notes, 1))
    print(acceder_element(notes, 10))

    eleve = {"nom": "Sara", "age": 20}
    print(acceder_cle(eleve, "nom"))
    print(acceder_cle(eleve, "email"))

    print(traiter_valeur("8"))
    print(traiter_valeur("x"))


main()