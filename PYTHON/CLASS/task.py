# 1. create a 3 unique classes with 3 unique static members
# 2. create 2 relative objects for that perticular class
# 3. create object methods to display prop of class as we 

class Car:
    wheels = 4
    fuel_type = "Petrol"
    brand = "BMW"

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        return f"Car Model: {self.model}, Color: {self.color}, Wheels: {Car.wheels}, Fuel Type: {Car.fuel_type}, Brand: {Car.brand}"

car1 = Car("M1", "Red")
car2 = Car("M2", "Blue")

print(car1.info())
print(car2.info())

class Bike:
    wheels = 2
    fuel_type = "Petrol"
    brand = "Yamaha"

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        return f"Bike Model: {self.model}, Color: {self.color}, Wheels: {Bike.wheels}, Fuel Type: {Bike.fuel_type}, Brand: {Bike.brand}"

bike1 = Bike("RX-100", "Black")
bike2 = Bike("MT-15", "White")

print(bike1.info())
print(bike2.info())

class Truck:
    wheels = 6
    fuel_type = "Diesel"
    brand = "MBenz"

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        return f"Truck Model: {self.model}, Color: {self.color}, Wheels: {Truck.wheels}, Fuel Type: {Truck.fuel_type}, Brand: {Truck.brand}"
    
truck1 = Truck("MB-5000", "Silver")
truck2 = Truck("MB-500xl", "Green")

print(truck1.info())
print(truck2.info())



def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
input = [1,2,3]
print(plus_one(input))
# input is [1,2,9] then output should be [1,3,0]
input = [1,2,9]
print(plus_one(input))
# input is [9,9,9] then output should be [1,0,0,0]
input = [9,9,9]
print(plus_one(input))