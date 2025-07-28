# PUBLIC CLASS ACCESS SPECIFIER -
'''class Company:
    C_name = 'Google'
    CEO = 'R.B'
    website = 'google.com'
    no_emp = 5000000
    turnover = 5000000000

    def __init__(self, n, ph, id, sal):
        self.name = n
        self.contact = ph
        self.empid = id
        self.salary = sal

    def disp(self):
        print(self.name, self.contact, self.empid, self.salary, sep='\n')

    @classmethod
    def display(cls):
        print(cls.C_name, cls.CEO, cls.website, cls.no_emp, cls.turnover, sep='\n')


# Create object
emp1 = Company('Rahul', 1234567890, 1234, 100000)

emp1.disp()
emp1.display()
'''


# PROTECTED CLASS ACCESS SPECIFIER -
'''class Company:
    C_name = 'Google'
    CEO = 'R.B'
    website = 'google.com'
    _no_emp = 5000000
    _turnover = 5000000000

    def __init__(self, n, ph, id, sal):
        self.name = n
        self.contact = ph
        self.empid = id
        self._salary = sal

    def _disp(self):
        print(self.name, self.contact, self.empid, self._salary, sep='\n')

    @classmethod
    def display(cls):
        print(cls.C_name, cls.CEO, cls.website, cls._no_emp, cls._turnover, sep='\n')


# Create object
emp1 = Company('Rahul', 1234567890, 1234, 100000)

emp1._disp()
emp1.display()
'''

# PRAVATE CLASS ACCESS SPECIFIERS -
'''class Company:
    C_name = 'Google'
    CEO = 'R.B'
    website = 'google.com'
    __no_emp = 5000000
    __turnover = 5000000000

    def __init__(self, n, ph, id, sal):
        self.name = n
        self.contact = ph
        self.empid = id
        self.__salary = sal

    def __disp(self):
        print(self.name, self.contact, self.empid, self.__salary, sep='\n')

    @classmethod
    def display(cls):
        print(cls.C_name, cls.CEO, cls.website, cls.__no_emp, cls.__turnover, sep='\n')


# Create object
emp1 = Company('Rahul', 1234567890, 1234, 100000)

emp1.__disp()
emp1.display()

# ACCESSING PRIVATE MEMBERS OF THE CLASS 
# 1. Syntax Method 

Cname._Cname__prop/mname()
obj._cname__prop/mname()'''

# GETTERS AND SETTERS
class Company:
    C_name = 'Google'
    CEO = 'R.B'
    website = 'google.com'
    __no_emp = 5000000
    __turnover = 5000000000

    def __init__(self, n, ph, id, sal):
        self.name = n
        self.contact = ph
        self.empid = id
        self.__salary = sal

    def __disp(self):
        print(self.name, self.contact, self.empid, self.__salary, sep='\n')

    @classmethod
    def display(cls):
        print(cls.C_name, cls.CEO, cls.website, cls.__no_emp, cls.__turnover, sep='\n')

    def getter(self):
        return self.__salary
    
    def setter(self, New):
        self.__salary = New


# Create object
emp1 = Company('Rahul', 1234567890, 1234, 100000)
print("Employee Salary:", emp1.getter())
emp1.setter(150000)
print(emp1.getter)




'''GETTERS - ACCESING THE PRIVATE MEMBERS
SETTERS - MODIFY THE PRIVATE MEMBERS'''

