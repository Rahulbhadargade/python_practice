'''class father:
      prop1 = "House"
      prop2 = "Car"
      
      def display(self):
            print(self.prop1, self.prop2)
            
class child(father):
      pro1 ="Cycle"
      prp2 = "Mobile"
      
child1 = child()
child1.display()

child2 = father()
child2.display()

print(child1.pro1,child1.prop2)
'''
#create a class named grand father, create a class called father, in grandfather class store three properties, in father class store three properties after that inherite the properties of grandfather class to father class and print all the properties that are available for father
'''class grandfather:
      prop1 = "Farm"
      prop2 = "Gold"
      prop3 = "House"
      prop4 = "GOV Job"

class father(grandfather):
      pro1 = "Car"
      pro2 = "Bike"
      pro3 = "Mobile"
      
class child(father):
      p1 = "Clothes"
      p2 = "cycle"
      p3 = "Degree"
      
obj = child()
print(f"Me : {obj.prop1},{obj.prop2},{obj.prop3},{obj.pro1},{obj.pro2},{obj.pro3},{obj.p1},{obj.p2},{obj.p3}")
'''

# 1. create a class called grandfatherwith his properties and method to display them
# 2. create a class called father with his properties and a method to display them and inherit the properties from the grandfather class
# 3. create a class called mother with her properties and method to display them
# 4. create a class called child with his properties and method to display them and inherite the properties from the father class and the mother class 
# 5. create an object of the child class and access all the display methods of the child, father, mother and grandfather classes
'''class Grandfather:
    def __init__(self) -> None:
        self.prop1 = "Farm"
        self.prop2 = "Gold"
        self.prop3 = "House"

    def display(self):
        print(f"Grandfather Properties: {self.prop1}, {self.prop2}, {self.prop3}")

class Father(Grandfather):
    def __init__(self) -> None:
        super().__init__()
        self.pro1 = "Car"
        self.pro2 = "Bike"
        self.pro3 = "Mobile"

    def display(self):
        print(f"Father Properties: {self.prop1}, {self.prop2}, {self.prop3}, {self.pro1}, {self.pro2}, {self.pro3}")
        super().display()

class Mother:
    def __init__(self) -> None:
        self.MPro1 = "Jewelry"
        self.MPro2 = "Kitchen"
        self.MPro3 = "Clothes"

    def display(self):
        print(f"Mother Properties: {self.MPro1}, {self.MPro2}, {self.MPro3}")

class Child(Father, Mother):
    def __init__(self) -> None:
        Father.__init__(self)
        Mother.__init__(self)
        self.CPro1 = "Toys"
        self.CPro2 = "Books"
        self.CPro3 = "Games"

    def display(self):
        print(f"Child Properties: {self.CPro1}, {self.CPro2}, {self.CPro3}")
        Father.display(self)
        Mother.display(self)
        Grandfather.display(self)

child = Child()
child.display()
'''
class ssc:
      def __init__(self,n, ph, ss_no, ssc):
            self.name = n
            self.phone = ph
            self.ssc_seat_no = ss_no
            self.ssc_Marks = ssc
            
class hsc(ssc):
      def __init__(self, n, ph, ss_no, ssc, hs_no, hsc):
            super().__init__(n, ph, ss_no, ssc)
            self.hs_no = hs_no
            self.hsc_Marks = hsc
            
class degree(hsc):
      def __init__(self, n, ph, ss_no, ssc, hs_no, hsc, ds_no, deg):
            super().__init__( n, ph, ss_no, ssc, hs_no, hsc)
            self.degree_seat_no = ds_no
            self.deg_Marks = deg