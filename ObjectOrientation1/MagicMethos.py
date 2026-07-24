# dunder methods --> 

def add():
    a = 10
    a = a+5
    print(a)
if __name__ == '__main__':
    add()

a = 5
b = 10
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__div__(b))


# example 1: this is int class -->
# # addition how internally is makes
def main():
    a = 5
    # a = a + 5 
    a = a.__add__(5) # using 'dunder add'
    print(a)
main()


# example 02: this is str class --> 
# addition on string
def main():
    s = 'mala'
    # s = s + 'tesh' # programmer see this 
    s = s.__add__('tesh') # internally this dunder add happens
    print(s)
main()


# example 03: adding two points in graph 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def display(self):
        print(self.__dict__)
def main():
    p1 = Point(2,3)
    p2 = Point(1,1)
    p3 = p1+p2
    p3.display()
if __name__ == '__main__':
    main()

# if you don't give display method --> object is in print statement
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self): #string representation
        return f'[x={self.x},y={self.y}]'
    def __repr__(self):
        return f'{type(self)} {id(self)}'
def main():
    p1 = Point(1,1)
    p2 = Point(1,1)
    print(p1.__repr__())
    print(p2.__repr__())
if __name__ == '__main__':
    main()