# 51. Create a Student class with attributes and methods.
# 52. Create a BankAccount class with deposit() and withdraw() methods.
# 53. Demonstrate inheritance using Person and Employee classes.
# 54. Demonstrate method overriding.
# 55. Demonstrate polymorphism using different shapes.
# 56. Implement encapsulation using private variables.
# 57. Demonstrate abstraction using the abc module.
# 58. Create a class to calculate the area of different shapes.
# 59. Implement constructor and destructor in a class.
# 60. Demonstrate operator overloading.
# 51. Create a Student class with attributes and methods.
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
student = Student("Malatesh", 22, 90)
student.display()

# 52. Create a BankAccount class with deposit() and withdraw() methods.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance after withdrawal:", self.balance)
        else:
            print("Insufficient Balance")
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)

# 53. Demonstrate inheritance using Person and Employee classes.
class Person:
    def display(self):
        print("I am a Person")
class Employee(Person):
    def work(self):
        print("I am an Employee")
employee = Employee()
employee.display()
employee.work()

# 54. Demonstrate method overriding.
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
dog = Dog()
dog.sound()

# 55. Demonstrate polymorphism using different shapes.
class Circle:
    def area(self):
        print("Area of Circle")
class Rectangle:
    def area(self):
        print("Area of Rectangle")
for shape in (Circle(), Rectangle()):
    shape.area()

# 56. Implement encapsulation using private variables.
class Employee:
    def __init__(self):
        self.__salary = 50000
    def display(self):
        print("Salary:", self.__salary)
employee = Employee()
employee.display()

# 57. Demonstrate abstraction using the abc module.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def area(self):
        print("Area of Square")
square = Square()
square.area()

# 58. Create a class to calculate the area of different shapes.
class Area:
    def circle(self, r):
        print("Area of Circle =", 3.14 * r * r)
    def rectangle(self, l, b):
        print("Area of Rectangle =", l * b)
    def square(self, s):
        print("Area of Square =", s * s)
area = Area()
area.circle(5)
area.rectangle(4, 6)
area.square(5)

# 59. Implement constructor and destructor in a class.
class Demo:
    def __init__(self):
        print("Constructor Called")
    def __del__(self):
        print("Destructor Called")
obj = Demo()
del obj

# 60. Demonstrate operator overloading.
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)
print("Sum =", n1 + n2)