# ENCAPSULATION : access is there but in controlled manner
# --> providing access but in controlled way bcz missuse cannot happen. using getter setter.
# --> something get you the value, something you can set the value.using these two we access in controlled manner.

# EXAMPLE : 1
class AccountHolder:
    def __init__(self):
        self.balance = 10000
    def get_balance(self):
        return self.balance
    def set_balance(self,amount):
        if amount > 0:
            self.balance = amount
        else:
            print('invalid amount')
ah = AccountHolder()
print(ah.get_balance())
ah.set_balance(-20000)
print(ah.get_balance())

'''below lines not secure bcz balance add and remove not easy thing '''
# print(ah.balance)
# ah.balance = -20000
# print(ah.balance)

# EXAMPLE : 2
class BankAccount:
    def __init__(self,balance):
        self._balance = balance # private variable # under score '_' --> private variable do not directly access.
    def Deposite(self,amount):
        self._balance = self._balance + amount
    def get_balance(self):
        return self._balance
amount = BankAccount(1000)
print(amount.get_balance)
amount.Deposite(500)
print(amount.get_balance())

# EXAMPLE : 3
class AccountHolder:
    def __init__(self):
        self.__balance = 10000 # data mangling --> double underscore before balance. 
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount > 0:
            self.__balance = amount
        else:
            print('invalid amount')
ah = AccountHolder()
ah.__balance = 20000 # ah.__dict__['__balance'] = 20000
print(ah.__dict__) # '_AccountHolder__balance': 10000, '__balance': 20000 --> brand new created 
print(ah._AccountHolder__balance) # data mangling 

# EXAMPLE : 4
class AccountHolder:
    def __init__(self):
        self.__balance = 10000 # data mangling --> double underscore before balance. 
    def get_balance(self):
        print('get_balance() called')
        return self.__balance
    def set_balance(self,amount):
        print('set_balance() called')
        if amount > 0:
            self.__balance = amount
        else:
            print('invalid amount')
    bal = property(get_balance,set_balance)
ah = AccountHolder()
print(ah.bal)
ah.bal = 20000
print(ah.bal)


# EXAMPLE : 5 --> use decorator --> 'property' and '@balance.setter
class AccountHolder:
    def __init__(self):
        self.__balance = 10000 # data mangling --> double underscore before balance. 
    @property
    def balance(self):
        print('get_balance() called')
        return self.__balance
    @balance.setter
    def balance(self,amount):
        print('set_balance() called')
        if amount > 0:
            self.__balance = amount
        else:
            print('invalid amount')
    bal = property(balance,balance)
ah = AccountHolder()
print(ah.balance)
ah.balance = 20000
print(ah.balance)