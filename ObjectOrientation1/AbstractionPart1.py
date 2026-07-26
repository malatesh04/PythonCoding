# CALCULATE THE AREA OF CIRCLE, RECTANGLE, TRIANGLE : NOT USING OOPS CONCEPT
from math import pi
class Circle:
    def __init__(self):
        self.r = 0
        self.area = 0
    def take_input(self):
        print('Calculating Circle : ')
        self.r = int(input('enter the radius\n'))
    def find_area(self):
        self.area = pi*self.r*2
    def disp_area(self):
        print(f'Circle Area --> {self.area}')
class Rectangle:
    def __init__(self):
        self.l = 0
        self.b = 0
        self.area = 0
    def take_input(self):
        print('Calculating Rectangle : ')
        self.l = int(input('enter a length\n'))
        self.b = int(input('enter a breadth\n'))
    def find_area(self):
        self.area = self.l * self.b
    def disp_area(self):
        print(f'Rectangle area --> {self.area}')
class Triangle:   
    def __init__(self):
        self.h = 0
        self.b = 0
        self.area = 0
    def take_input(self):
        print('Calculating Triangle : ')
        self.h = int(input('enter height\n'))
        self.b = int(input('enter a base\n'))
    def find_area(self):
        self.area = (self.h * self.b)/2
    def disp_area(self):
        print(f'Triangle area --> {self.area}')
def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()
    c.take_input()
    c.find_area()
    c.disp_area()
    r.take_input()
    r.find_area()
    r.disp_area() 
    t.take_input()
    t.find_area()
    t.disp_area()    
main()

# CALCULATE THE AREA OF CIRCLE, RECTANGLE, TRIANGLE : USING OOPS CONCEPT 
from math import pi
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self):
        self.area = 0
    @abstractmethod 
    def take_input(self):
        pass
    @abstractmethod
    def find_area(self):
        pass
    @abstractmethod
    def disp_area(self):
        pass
class Circle(Shape):
    def __init__(self):
        self.r = 0
        # self.area = 0
        super().__init__()
    def take_input(self):
        print('Calculating Circle : ')
        self.r = int(input('enter the radius\n'))
    def find_area(self):
        self.area = pi*self.r*2
    def disp_area(self):
        print(f'Circle Area --> {self.area}')
class Rectangle(Shape):
    def __init__(self):
        self.l = 0
        self.b = 0
        # self.area = 0
        super().__init__()
    def take_input(self):
        print('Calculating Rectangle : ')
        self.l = int(input('enter a length\n'))
        self.b = int(input('enter a breadth\n'))
    def find_area(self):
        self.area = self.l * self.b
    def disp_area(self):
        print(f'Rectangle area --> {self.area}')
class Triangle(Shape):   
    def __init__(self):
        self.h = 0
        self.b = 0
        # self.area = 0
        super().__init__()
    def take_input(self):
        print('Calculating Triangle : ')
        self.h = int(input('enter height\n'))
        self.b = int(input('enter a base\n'))
    def find_area(self):
        self.area = (self.h * self.b)/2
    def disp_area(self):
        print(f'Triangle area --> {self.area}')
def geometric_shape(ref):
    ref.take_input()
    ref.find_area()
    ref.disp_area()
def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()
    # use polymorphism : 
    geometric_shape(c)
    geometric_shape(r)
    geometric_shape(t)  
main()