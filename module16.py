

class Vehicle:
    def __init__(self,brand,registration):
        self.brand = brand
        self.registration = registration
    def daily_rate(self):
        pass

class Car(Vehicle):
    def __init__(self,brand,registration,number_seats):
        super().__init__(brand,registration)
        self.number_seats = number_seats
        self.price = 20 + number_seats*5
    def daily_rate(self):
        return self.price
    def __str__(self):
        return f"{self.brand} Car ({self.registration}) -- {self.number_seats} places -- {self.daily_rate()}/day"

class Motorcycle(Vehicle):
    def __init__(self,brand,registration,cylinder):
        super().__init__(brand,registration)
        self.cylinder = cylinder
        self.price = 20 + cylinder*5
    def daily_rate(self):
        return self.price

class Truck(Vehicle):
    def __init__(self,brand,registration,payload):
        super().__init__(brand,registration)
        self.payload = payload
        self.price = 20 + payload*5
    def daily_rate(self):
        return self.price

# car = Car("Renault", "123-A-45", number_seats=5)
# motorcycle = Motorcycle("Yamaha", "987-B-65", cylinder=600)
# truck = Truck("Volvo", "456-C-78", payload=3000)
# print(car.brand)
# print(car.daily_rate())
# print(motorcycle.daily_rate())
# print(truck.daily_rate())

# fleet = [
#     Car("Renault", "123-A-45", number_seats=5),
#     Motorcycle("Yamaha", "987-B-65", cylinder=600),
#     Truck("Volvo", "456-C-78", payload=3000)
# ]
# for v in fleet:
#     print(f"{v.brand} -> {v.daily_rate()}")

print(Car("Renault", "123-A-45", number_seats=5))