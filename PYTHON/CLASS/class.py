# 1. create a 3 unique classes with 3 unique static members
# 2. create 2 relative objects for that perticular class
# 3. create object methods to display prop of class as we 
'''class Car:
    wheels = 4
    fuel_type = "Petrol"
    brand = "Toyota"

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        return f"Car Model: {self.model}, Color: {self.color}, Wheels: {Car.wheels}, Fuel Type: {Car.fuel_type}, Brand: {Car.brand}"
class Bike:
    wheels = 2
    fuel_type = "Petrol"
    brand = "Yamaha"

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        return f"Bike Model: {self.model}, Color: {self.color}, Wheels: {Bike.wheels}, Fuel Type: {Bike.fuel_type}, Brand: {Bike.brand}"
class Truck:
    wheels = 6
    fuel_type = "Diesel"
    brand = "Ford"

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        return f"Truck Model: {self.model}, Color: {self.color}, Wheels: {Truck.wheels}, Fuel Type: {Truck.fuel_type}, Brand: {Truck.brand}"
# Creating objects for each class
car1 = Car("Corolla", "Red")
car1.__init__("Corolla", "Red")
car2 = Car("Camry", "Blue")
car2.__init__("Camry", "Blue")
bike1 = Bike("YZF-R3", "Black")
bike2 = Bike("MT-07", "White")
truck1 = Truck("F-150", "Silver")
truck2 = Truck("Ranger", "Green")
# Displaying information about each vehicle
print(car1.info())
print(car2.info())
print(bike1.info())
print(bike2.info())
print(truck1.info())
print(truck2.info())
'''

'''class Bank:
    bank_name = "Fedaral"
    branch = "DC"
    ifsc = "FED00001234"
    website = "www.fed.in"

    def display(self):
        print("Name:", self.name)
        print("Phone:", self.ph)
        print("Account Number:", self.acc_no)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)
        print()


cus1 = Bank()
cus1.name = "A"
cus1.ph = "9012345678"             
cus1.acc_no = "FED123456789"       
cus1.acc_type = "Savings"
cus1.balance = 20000               

cus2 = Bank()
cus2.name = "B"
cus2.ph = "9988776655"             
cus2.acc_no = "FED987654321"       
cus2.acc_type = "Current"
cus2.balance = 30000              

cus1.display()
cus2.display()'''

'''class Bank:
    bank_name = "Fedaral"
    branch = "DC"
    ifsc = "FED00001234"
    website = "www.fed.in"

    @classmethod
    def dis(cls):
        print("Bank Name:", cls.bank_name)
        print("Branch:", cls.branch)
        print("Website:", cls.website)

    @classmethod
    def upd(cls, name, branch, website):
        cls.bank_name = name
        cls.branch = branch
        cls.website = website

Bank.dis()

Bank.upd("HDFC Bank", "Mumbai", "www.hdfc.com")

Bank.dis()'''

'''class Bank:
    bank_name = "Fedaral"
    branch = "DC"
    ifsc = "FED00001234"
    website = "www.fed.in"

    @classmethod
    def dis(cls):
        print("Bank Name:", cls.bank_name)
        print("Branch:", cls.branch)
        print("Website:", cls.website)

    @classmethod
    def upd(cls, name, branch, website):
        cls.bank_name = name
        cls.branch = branch
        cls.website = website

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)

    @staticmethod
    def subtract(x, y):
        print("Result:", x - y)

Bank.dis()
Bank.upd("HDFC Bank", "Mumbai", "www.hdfc.com")
Bank.dis()

cus1 = Bank()
cus1.name = "Rahul"
cus1.balance = 5000
cus1.withdraw(2000)

Bank.subtract(10, 3)
'''


class Bank:
    bank_name = "Fedaral"
    branch = "DC"
    ifsc = "FED00001234"
    website = "www.fed.in"

    @classmethod
    def dis(cls):
        print("Bank Name:", cls.bank_name)
        print("Branch:", cls.branch)
        print("Website:", cls.website)

    @classmethod
    def upd(cls, name, branch, website):
        cls.bank_name = name
        cls.branch = branch
        cls.website = website

Bank.dis()

Bank.upd("HDFC Bank", "Mumbai", "www.hdfc.com")

Bank.dis()



# TASK - 
# create a new class "banking"
# create two class members (bank name, ifsc)
# create a two object 
# create three object members(cname, c_acc, bal = 5000)

# perform thise operations 
# with respect to custumer one
# print(cust1.display())
# deposite 20000
# print(cust1.display())
# widraw 17000
# print(cust1.display())
# widraw 5000
# print(cust1.display())
# diposite 15000

# perform thise operations 
# with respect to custumer one
# print(cust1.display())
# deposite 50000
# print(cust1.display())
# widraw 55000
# print(cust1.display())
# widraw 5000
# print(cust1.display())
# diposite 100000
