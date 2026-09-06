





def verifier_age(age):
    if(age<0): raise ValueError(f'Age cannot be negative ({age}).')
    return age
def traiter_liste_de_valeurs(liste):
    for item in liste:
        item = int(item)
    return liste
class StockInsuffisantError(Exception):
    def __init__(self, product, quantity, available):
        self.available = available
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return (
            f'Stock insuffisant pour "{self.product}" '
            f"(demande: {self.quantity}, disponible: {self.available})"
        )
def retirer_stock(stock,product,quantity):
    available = stock[product]
    if available >= quantity:
        available -= quantity
        return f"Retrait effectue: {quantity} {product}"
    raise StockInsuffisantError(product,quantity,available)
def main():
    stock = {"pommes": 20, "bananes": 4}

    # try:
    #     print('Age Verified: ',verifier_age(30))
    # except ValueError as e:
    #     print(e)
    
    # try:
    #     print('Age Verified: ',verifier_age(-3))
    # except ValueError as e:
    #     print(e)

    # try:
    #     print(traiter_liste_de_valeurs(["3", "9", "x", "5"]))
    # except ValueError:
    #     print('Log : valeur "x" invalide, exception relancee.')
    #     raise

    try:
        print(retirer_stock(stock, "pommes", 5))
    except StockInsuffisantError as e:
        print(f'{type(e).__name__}: {e}')

    try:
        print(retirer_stock(stock, "bananes", 10))
    except StockInsuffisantError as e:
        print(f'{type(e).__name__}: {e}')


    

main()