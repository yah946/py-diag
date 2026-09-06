
class StockInsuffisantError(Exception):
    def __init__(self, product, quantity, available):
        self.available = available
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return (
            f'[ERROR] Stock insuffisant pour "{self.product}" '
            f"(demande: {self.quantity}, disponible: {self.available})"
        )
def retirer_stock(stock,product,quantity):
    if(quantity.isalpha()): raise ValueError(f'[ERROR]{product}: entred quantity is invalid ("{quantity}")')
    else: quantity = int(quantity)
    if(product not in stock): raise KeyError(f'[ERROR]{product}: product not exist')
    available = stock[product]
    if available >= quantity:
        available -= quantity
        return True
    raise StockInsuffisantError(product,quantity,available)
def safe_retrait(stock,product,quantity):
    with open('journal.txt','a',encoding='utf-8') as f:
        try:
            retirer_stock(stock, product, quantity)
        except StockInsuffisantError as e:
            f.write(str(e)+'\n')
        except KeyError as e:
            f.write(str(e.args[0])+'\n')
        except ValueError as e:
            f.write(str(e)+'\n')
        else:
            f.write(f"[OK] Retrait effectue: {quantity} {product}, reste({stock[product]})"+'\n')
def read_journal(path):
    with open(path,'r',encoding='utf-8') as f:
        contents = f.read()
    return contents
def main():
    stock = {"pommes": 20, "bananes": 4, "oranges": 15}
    commandes_brutes = [
        "pommes,5",
        "bananes,10",
        "kiwis,2",
        "oranges,abc",
        "oranges,5",
    ]
    for order in commandes_brutes:
        product = order.split(',')[0]
        quantity = order.split(',')[1]
        safe_retrait(stock,product,quantity)
    
    print(read_journal('journal.txt'))



main()