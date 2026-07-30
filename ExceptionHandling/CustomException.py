''' custom exception '''
'''steps'''
'''creat a class give suitable name in camel case(first letter of every letter is capital letter) and end with error
and inherit exception class then wherever u want exception to be generate just raise it'''

# Example 1:
class InvalidMobileNumberError(Exception):
    pass

def validate(mob):
    if len(mob) == 10:
        print('valid number')
    else:
        raise InvalidMobileNumberError('Enter 10 digit numer')
def main():
    mob = input()
    validate(mob)
main()

# Example 2:
class NotInListError(Exception):
    pass
def menu(item):
    if item == 'pizza':
        print('enjoy pizza')
    elif item == 'idli':
        print('enjoy idli')
    elif item == 'burger':
        print('enjoy burger')
    else:
        raise NotInListError('You typed item is not present in menu')
def main():
    item = input()
    try:
        menu(item)
    except NotInListError as e :
       print(e) 
main()

# Example 2:
class DuplicateUserError(Exception):
    pass
class WeakPasswordError(Exception):
    pass
class user:
    user_name = set()
    def __init__(self,un,mob,pwd):
        self.un = un
        self.mob = mob
        self.pwd = pwd
        self.add_user()
        self.validate_password()
    def add_user(self):
        if self.un in user.user_name:
            raise DuplicateUserError('user name already exist')
        else:
            user.user_name.add(self.un)
    def validate_password(self):
        uc=lc=sp=num=0
        for i in self.pwd:
            if i.isupper():
                uc += 1
            elif i.islower():
                lc += 1
            elif i.isdigit():
                num += 1
            else:
                sp += 1
        if len(self.pwd) < 6 or uc == 0 or lc == 0 or num == 0 or sp == 0:
            raise WeakPasswordError('Password not strong')
def main():
    un = input('enter name\n')
    mob = int(input('enter phone number\n'))
    pwd = input('enter password\n')
    try:
        u1 = user(un,mob,pwd)
        u2 = user(un,mob,pwd)
    except DuplicateUserError as e:
        print(e)
    except WeakPasswordError as e:
        print(e)
    except:
        print('some issue occures')
    else:
        print('Account Created Successfully')
main()
