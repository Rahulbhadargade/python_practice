#create a class on based real world objects and create 2 objects in that class

'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2021)
def display_info(car):
    return f"{car.year} {car.make} {car.model}"
print(display_info(car1))
print(display_info(car2))

class Car:
    brand = ""
    model = ""
    color = ""
    year = 0

# Create first car object
car1 = Car()
car1.brand = "Toyota"
car1.model = "Camry"
car1.color = "Red"
car1.year = 2022

# Create second car object
car2 = Car()
car2.brand = "Honda"
car2.model = "Civic"
car2.color = "Blue"
car2.year = 2021

# Print details
print(car1.brand, car1.model, car1.color, car1.year)
print(car2.brand, car2.model, car2.color, car2.year)
'''

'''class Company:
    c_name = "Test Yantra"
    loc = "Mumbai"
    industry = "Software Development"

    def display(self):
        print("Company Details")
        print("Company Name:", Company.c_name)
        print("Location:", Company.loc)
        print("Industry:", Company.industry)

        print("Employee Details")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Role:", self.role)
        print()

emp1 = Company()
emp1.name = "Rahul"
emp1.emp_id = 101
emp1.role = "Software Engineer"

emp2 = Company()
emp2.name = "Divya"
emp2.emp_id = 102
emp2.role = "UI/UX Designer"

emp3 = Company()
emp3.name = "Arjun"
emp3.emp_id = 103
emp3.role = "Manager"

emp1.display()
emp2.display()
emp3.display()
'''
#crete 50 objects and 3 objects members for all 50 objects 

class Employee:
    def __init__(self, name, emp_id, role):
        self.name = name
        self.emp_id = emp_id
        self.role = role

    def display(self):
        print("Name:", self.name, "ID:", self.emp_id, "Role:", self.role)


# Creating 50 objects
emp1 = Employee("Rahul", 1001, "CEO")
emp2 = Employee("Divya", 1002, "Manager")
emp3 = Employee("Arjun", 1003, "Tester")
emp4 = Employee("Srushti", 1004, "Designer")
emp5 = Employee("Sahil", 1005, "Developer")
emp6 = Employee("Satish", 1006, "analyst")
emp7 = Employee("Tanmay", 1007, "signal engineer")
emp8 = Employee("Sanika", 1008, "graphics designer")
emp9 = Employee("Mrudula", 1009, "quality analyst")
emp10 = Employee("Pranavi", 1010, "web developer")
emp11 = Employee("Pranjal", 1011, "frontend developer")
emp12 = Employee("Snehal", 1012, "backend developer")
emp13 = Employee("Prajwal", 1013, "middleware developer")
emp14 = Employee("Ritesh", 1014, "DevOps Engineer")
emp15 = Employee("Sourabh", 1015, "oracle cloud engineer")
emp16 = Employee("Shubham", 1016, "Data Scientist")
emp17 = Employee("Kartik", 1017, "Data Analyst")
emp18 = Employee("Virat", 1018, "Project Manager")
emp19 = Employee("Rohit", 1019, "cloud engineer")
emp20 = Employee("Thala", 1020, "security Engineer")
emp21 = Employee("Dinga", 1021, "Marketing Manager")
emp22 = Employee("Dingi", 1022, "cyber security analyst")
emp23 = Employee("Pradeep", 1023, "maintenance Engineer")
emp24 = Employee("Mohit", 1024, "trainer")
emp25 = Employee("Rohit", 1025, "Developer")
emp26 = Employee("Mehak", 1026, "Tester")
emp27 = Employee("Colin", 1027, "Manager")
emp28 = Employee("Vitthal", 1028, "chai-coffee")
emp29 = Employee("Pratiksha", 1029, "chairman")
emp30 = Employee("Sanjay", 1030, "task manager")
emp31 = Employee("Baburao", 1031, "security guard")
emp32 = Employee("Vaishali", 1032, "field engineer")
emp33 = Employee("Ekta", 1033, "trainee")
emp34 = Employee("Priti", 1034, "visiter")
emp35 = Employee("Datta", 1035, "technical support")
emp36 = Employee("Preet", 1036, "database administrator")
emp37 = Employee("Bhanupratap", 1037, "network engineer")
emp38 = Employee("Shital", 1038, "intern")
emp39 = Employee("Idali", 1039, "kuch samj ni aaya")
emp40 = Employee("Vada", 1040, "Khaloo")
emp41 = Employee("Sambar", 1041, "Testy")
emp42 = Employee("Chatani", 1042, "Very hot")
emp43 = Employee("Dosa", 1043, "My fav")
emp44 = Employee("Vaishanvi", 1044, "graphics designer")
emp45 = Employee("Kiran", 1045, "Project Coordinator")
emp46 = Employee("Baban", 1046, "office boy")
emp47 = Employee("Rushi", 1047, "HR Manager")
emp48 = Employee("Shashi", 1048, "Receptionist")
emp49 = Employee("Gauri", 1049, "Accountant")
emp50 = Employee("Shankar", 1050, "Logistics Manager")

# Display the details of all employees
emp1.display()
emp2.display()
emp3.display()
emp4.display()
emp5.display()
emp6.display()
emp7.display()
emp8.display()
emp9.display()
emp10.display()
emp11.display()
emp12.display()
emp13.display()
emp14.display()
emp15.display()
emp16.display()
emp17.display()
emp18.display()
emp19.display()
emp20.display()
emp21.display()
emp22.display()
emp23.display()
emp24.display()
emp25.display()
emp26.display()
emp27.display()
emp28.display()
emp29.display()
emp30.display()
emp31.display()
emp32.display()
emp33.display()
emp34.display()
emp35.display()
emp36.display()
emp37.display()
emp38.display()
emp39.display()
emp40.display()
emp41.display()
emp42.display()
emp43.display()
emp44.display()
emp45.display()
emp46.display()
emp47.display()
emp48.display()
emp49.display()
emp50.display()