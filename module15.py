

class BankAccount:
    bank_name = "PyDiagBank"
    counter = 0
    def __init__(self,name,sold):
        self.name = name
        self.__sold = sold
        BankAccount.counter+=1

    @property
    def sold(self):
        return self.__sold
    def deposit(self,price):
        if price > 0:
            self.__sold += price
        else: raise ValueError(f"Price Cannot Be Negative ({price})!")
    def retrait(self,price):
        if price < 0:
            raise ValueError(f"Price Cannot Be Negative ({price})!")
        if price > self.__sold:
            raise ValueError(f"Insufficient funds (balance: {self.sold}, withdrawal request: {price})!")
            self.__sold -= price
        self.__sold -= price

    @classmethod
    def number_of_accounts(cls):
        return cls.counter
    @staticmethod
    def convert_currency(sold,rate):
        return sold*rate


# account = BankAccount("Adam",sold=100)
# print(account.sold)
# account.sold = 5000

# account = BankAccount("Adam",sold=100)
# account.deposit(50)
# account.retrait(30)
# print(account.sold)

# account = BankAccount("Adam",sold=100)
# try:
#     account.deposit(-50)
# except ValueError as e:
#     print(e)
# try:
#     account.retrait(300)
# except ValueError as e:
#     print(e)

# a1 = BankAccount("Ali",100)
# a2 = BankAccount("Othman",200)
# print(a1.bank_name,a2.bank_name)
# print(a1.sold,a2.sold)

a1 = BankAccount("Ali",100)
a2 = BankAccount("Othman",200)
a3 = BankAccount("Omar",0)
print(f"Number of accounts is: {BankAccount.number_of_accounts()} account(s)")
print(f"Convert currency: {BankAccount.convert_currency(100,10.5)}")