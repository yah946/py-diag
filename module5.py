def sell(stock_list,product_name,quantity):
    if quantity <= stock_list[product_name]:
        stock_list[product_name] -= quantity
        print(f'Recorded sale: 20 {product_name}.')
    else:
        print(f'Insufficient stock for {product_name} (available: {stock_list[product_name]}).')
def serach_products_out_of_stock(stock_list):
    products_out_of_stock = []
    for key,value in stock_list.items():
        if value == 0:
            products_out_of_stock.append(key)
    return products_out_of_stock
def total_per_client(orders):
    total = {}
    for order in orders:
        if order['client'] in total:
            total[order['client']] += order['quantite']
        else:
            total[order['client']] = order['quantite']
    return total
def dictionary_inverting(d):
    return {value: key for key,value in d.items()}
def print_number_of_employees_in_each_domain(entreprise):
    for domain,employees in entreprise.items():
        print(f'{domain}: {len(employees)} employee(s)')

...

def main():

    stock =  {"apples": 50, "bananas": 0, "oranges": 0, "kiwis": 12}
    orders = [
        {"client": "Ali", "produit": "pommes", "quantite": 5},
        {"client": "Sara", "produit": "bananes", "quantite": 10},
        {"client": "Ali", "produit": "oranges", "quantite": 2},
    ]
    words = ["chat", "elephant", "abeille", "riz"]
    entreprise = {
        "IT": ["Ali", "Sara", "Omar"],
        "RH": ["Lina"],
        "Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
    }


    # sell(stock, "apples", 20)
    # sell(stock, "oranges", 5)

    # print(serach_products_out_of_stock(stock))

    # print(total_per_client(orders))

    # print(dictionary_inverting({"a": 1, "b": 2, "c": 3}))

    # print({word: len(word) for word in words})

    # print_number_of_employees_in_each_domain(entreprise)


main()