class prop:
    def __init__(self):
        self.__a = 10
        self.__b = 20

    def __disp(self):
        print("This is private method to display")

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, new):
        self.__a = new

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, new):
        self.__b = new

    @property
    def disp(self):
        return self.__disp

# Example 1
obj = prop()
print("Initial obj.a:", obj.a)
print("Initial obj.b:", obj.b)
obj.a = 20
obj.b = 40
print("Updated obj.a:", obj.a)
print("Updated obj.b:", obj.b)

# Example 2: Property for another variable
class Demo:
    def __init__(self):
        self.__x = 5

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

demo_obj = Demo()
print("Initial demo_obj.x:", demo_obj.x)
demo_obj.x = 15
print("Updated demo_obj.x:", demo_obj.x)

# Example 3: Read-only property
class ReadOnly:
    def __init__(self):
        self.__val = 100

    @property
    def val(self):
        return self.__val

ro = ReadOnly()
print("ReadOnly val:", ro.val)

# Example 4: Property with validation
class Valid:
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self.__age = value

v = Valid()
print("Initial age:", v.age)
v.age = 25
print("Updated age:", v.age)
v.age = -5 

# Example 5: Property for computed value
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print("Rectangle area:", rect.area)
rect.width = 7
print("Updated rectangle area:", rect.area)