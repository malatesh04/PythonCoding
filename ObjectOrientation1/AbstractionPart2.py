from math import pi
class Circle:
    def __init__(self):
        self.r = 0
        self.area = 0
    def take_input(self):
        self.r = int(input('enter the radius\n'))
    def find_area(self):
        self.area = pi*(self.r**2)
    def disp_area(self):
        print(self.area)
class Rectangle:
    def __init__(self):
        self.l = 0
        self.b = 0
        self.area = 0
    def take_input(self):
        self.l = int(input('enter the length\n'))
        self.b = int(input('enter the breadth\n'))
    def find_area(self):
        self.area = self.l*self.b
    def disp_area(self):
        print(self.area)
class Triangle:
    def __init__(self):
        self.h = 0
        self.b = 0
        self.area = 0
    def take_input(self):
        self.h = int(input('enter the height\n'))
        self.b = int(input('enter the base\n'))
    def find_area(self):
        self.area = (self.h*self.b)/2
    def disp_area(self):
        print(self.area)
def all_method(ref):
    ref.take_input()
    ref.find_area()
    ref.disp_area()

def main():
    s1 = Circle()
    s2 = Rectangle()
    s3 = Triangle()
    all_method(s1)
    all_method(s2)
    all_method(s3)

    # s1.take_input()
    # s1.find_area()
    # s1.disp_area()

    # s2.take_input()
    # s2.find_area()
    # s2.disp_area()

    # s3.take_input()
    # s3.find_area()
    # s3.disp_area()
main()