from abc import ABC, abstractmethod

class FundTransper(ABC):
    # GETTER SETTER FOR ACCOUNT_NUMBER -->
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    # GETTER -->
    @property
    def account_number(self):
        return self.__account_number
    # SETTER -->
    @account_number.setter
    def account_number(self,account_number):
        if len(str(account_number)) == 10:
            self.__account_number = account_number

    # GETTER SETTER FOR BALANCE -->
    # GETTER
    @property
    def balance(self):
        return self.__balance
    # SETTER
    @balance.setter
    def balance(self,balance):
        if balance > 0:
            self.__balance = balance

    '''def validate(self,amount):
        if len(str(self.account_number)) == 10 and amount < self.balance and amount > 0:
            return True
        else:
            return False'''
    def validate(self,amount):
        return len(str(self.account_number)) == 10 and amount < self.balance and amount > 0
    @abstractmethod
    def transper(self,amount):
        pass

class NEFTTransper(FundTransper):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    def transper(self, amount):
        sc = amount*0.05
        if (amount+sc) < self.balance:
            self.balance -= (amount+sc)
            return True
        else:
            return False
        
class IMPSTransper(FundTransper):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    def transper(self, amount):
        sc = amount*0.02
        if (amount+sc) < self.balance:
            self.balance -= (amount+sc)
            return True
        else:
            return False
        
class RTGSTransper(FundTransper):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
    def transper(self, amount):
        if amount < self.balance and amount >= 10000:
            self.balance -= amount
            return True
        else:
            return False
        
def main():
    an = int(input('enter a account number : \n'))
    balance = int(input('enter a account balance : \n'))
    print('enter your choise')
    print('1. NEFT\n2. IMPS\n3. RTGS\n')
    choise = int(input())

    if choise == 1:
        ref = NEFTTransper(an,balance)
    elif choise == 2:
        ref = IMPSTransper(an,balance)
    elif choise == 3:
        ref = RTGSTransper(an,balance)
    else:
        print('invalid choise')

    amt = int(input('enter the amount to be transfered\n'))

    if ref.validate(amt):
        if ref.transper(amt):
            print('transfer was successfully')
            print(f'Remaining balance : {ref.balance}')
        else:
            print('Transfer could not made')
    else:
        print('transfer amount seens to be wrong')

if __name__ == '__main__':
    main()