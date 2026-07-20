class Citizen:
    def __init__(self,name,age,gender,state,natinality):
        # creating instance variable
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state
        self.natinality = natinality

    # creating display function
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.state)
        print(self.natinality)


def main():
    malatesh = Citizen('malatesh',22,'male','karnataka','indian')
    swati = Citizen('swati',22,'female','maharastra','indian')
    rita = Citizen('rita',22,'female','keralam','indian')

    malatesh.display()
    swati.display()
    rita.display()


# when name == main then call the main() function.
if __name__ == '__main__':
    main()

''' 1st lyy main function is called then go to main function then when object is created then in 
stack __new__ dunder new is created in that all data stored in tuples then object is created 
inside the heap then call dunder __init__ argument is self created heap aaddress stored inside 
the self then they refer to heap object. __new__ is send all data to init in heap object the data 
store in the form of dictionary. now init work done then delete. then main function staart print 
the diplay() method.'''


# # here nationality is same for everyone like in india have 130 cr peoples 130 cr place in same object stored 
# # --> space complexity use--> 

class Citizen:

    # create static variable --> not under function 
    natinality = 'indian'

    def __init__(self,name,age,gender,state):
        # creating instance variable
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state

    # creating display function
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.state)
        print(self.natinality)

def main():
    malatesh = Citizen('malatesh',22,'male','karnataka')
    swati = Citizen('swati',22,'female','maharastra')
    rita = Citizen('rita',22,'female','keralam')
    malatesh.display()
    swati.display()
    rita.display()
    print(malatesh.__dict__)
    print(swati.__dict__)
    print(rita.__dict__)
    print(Citizen.__dict__)
    print(Citizen.__dict__['natinality']) # gives static variable
    print(malatesh.natinality) # gives static variable

# when name == main then call the main() function.
if __name__ == '__main__':
    main()

'''when u create another variable means one class one varible for common then citizen class 
variable is created in that have  dictionary like key value pairs.'''


# PROBLEMS 01 --> 

class Demo:
    a = 10
    b = 20

def main():
        print(Demo.a)
        print(Demo.b)
        Demo.a = 100
        Demo.b = 200
        print(Demo.a)
        print(Demo.b)
        
        d = Demo()
        print(d.a)
        print(d.b)

if __name__ == '__main__':
    main()
