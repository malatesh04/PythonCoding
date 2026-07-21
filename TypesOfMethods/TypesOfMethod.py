''' 
3 TYPES OF METHOD :
1 --> INSTANCE METHOD --> depend on the object
2 --> STATIC METHOD --> not depend on object
3 --> CLASS METHOD
'''

class BmwCar:
    def __init__(self,name,cc,color):
        self.name = name
        self.cc = cc
        self.color = color
    def start_engine(self):
        print(self.name,'engine is starting...')
    @staticmethod # using this built in decorator you can use calling function using class name or object name also.
    # these method doesn't dependecy in object.
    def kms_to_miles(kms): # this method not called using object uses --> class name dot function name.
        print(kms * 1.6)

def main():
    c = BmwCar('bmw',1200,'white')
    print(c.name)
    print(c.cc)
    print(c.color)
    c.start_engine() # BmwCar.start_engine(c)
    BmwCar.kms_to_miles(2) # uses class name for calling not a object
    c.kms_to_miles(2) # here when i call this that gives error bcz --> in function there is no self , or it converts --> BmwCar.kms_to_miles(c,2) here in function only one argumnets but in calling there are two arguments.
if __name__ == '__main__':
    main()

'''now class methods'''
class BmwCar:
    def __init__(self,name,cc,color):
        self.name = name
        self.cc = cc
        self.color = color
    @classmethod
    def x1(cls):
        return cls('x1',1998,'blue')
    @classmethod
    def series5(cls):
        return cls('series5',2993,'blue')
    @classmethod
    def i8(cls):
        return cls('i8',1499,'blue')
    def display(self):
        print(self.name)
        print(self.cc)
        print(self.color)
def main():
    c1 = BmwCar.x1()
    c2 = BmwCar.series5()
    c3 = BmwCar.i8()
    c1.display()
    c2.display()
    c3.display()

if __name__ == '__main__':
    main()