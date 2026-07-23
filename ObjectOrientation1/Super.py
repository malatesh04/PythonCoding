class Customer:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
class PlatinumCustomer(Customer):
    def __init__(self, name, phone, email,plat_id):
        super().__init__(name, phone, email)   # insted write this --> chaining --> child class constructer calling parents constucter.
        # self.name = name           }
        # self.phone = phone         } not write these lines 
        # self.email = email         }
        self.plat_id = plat_id
    def display(self):
        print(self.__dict__)
def main():
    p = PlatinumCustomer('malatesh',7676115923,'malateshbn178@gmail.com',6651)
    p.display()
if __name__ == '__main__':
    main()


class Customer:
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
    def place_order(self,dish):
        cost = 0
        del_charge = 50
        if dish == 'pizza':
            cost = 500 + del_charge
        else:
            cost = 250 + del_charge
        return cost
class PlatinumCustomer(Customer):
    def __init__(self, name, address, phone,plat_id):
        super().__init__(name, address, phone)
        self.place_id = plat_id 
    def place_order(self, dish):
        del_charge = 50
        return (super().place_order(dish) - del_charge)*0.95   # not take del_charge and givee 5% discount.
def main():
    p = PlatinumCustomer('malatesh','bengaluru',7676115923,6651)
    print(p.place_order('pizza'))

if __name__ == '__main__':
    main() 

# MULTILEVEL INHERITANCE :
class A:
    def fun(self):
        print('A')
class B(A):
    def fun(self):
        print('B')
class C(B):
    def fun(self):
        super(C,self).fun() # go to C classes parent here is B now print B class function.
        super(B,self).fun() # go to B classes parent is A now print A class function.
        print('C')
c = C()
c.fun()

# MULTIPLE INHERITANCE :
class A:
    def fun(self):
        print('A')
class B:
    def fun(self):
        print('B')
class C(A,B):
    def test(self):
        super().fun()
        print('C')
c = C()
c.test()
c.fun()