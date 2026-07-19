class Car:
    def __init__(self):
        self.brand = 'BMW'
        self.cc = 1200
        self.color = 'Blue'
    def start_engine(self):
        print(self.brand,"engine is starting...")
    def shift_gear(self):
        print(self.brand,"shifting gears...")
    def accelerate(self):
        print(self.brand,"is accelarating...")

def main():
    c1 = Car()
    print('brand:',c1.brand)
    print('cc:',c1.cc)
    print('color:',c1.color)
    c1.start_engine() # internally --> start_engine(c1) --> calling start_engine
    c1.shift_gear()
    c1.accelerate()

    c2 = Car()
    print('brand:',c2.brand)
    print('cc:',c2.cc)
    print('color:',c2.color)
    c2.start_engine() # internally --> start_engine(c2) --> calling start_engine
    c2.accelerate()
    c2.shift_gear()

if __name__ == '__main__':
    main()
