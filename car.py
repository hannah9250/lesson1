class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        print("This is a vehicle.")
        

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def describe(self):
        print("This is a car")


my_car = Car("Lexus", "RX")

print(my_car.brand)
print(my_car.model)
my_car.describe()

print(issubclass(Car, Vehicle))