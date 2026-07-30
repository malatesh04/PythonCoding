''' raise keyword '''
# Explicity to raise the exception --> abrupt termination.
 
def validate(mob):
    if len(mob) == 10:
        print('valid mobile number')
    else:
        raise ValueError
def main():
    mob = input('enter a number\n')
    validate(mob)
main()

def menu(item):
    if item == 'pizza':
        print('enjoy pizza')
    elif item == 'idli':
        print('enjoy idli')
    elif item == 'burger':
        print('enjoy burger')
    else:
        raise NameError
def main():
    item = input('enter item\n')
    menu(item)
main()

''' finaly keyword '''
def fun():
    print('fun() started execution')

    try:
        num = int(input('enter numerator\n'))
        den = int(input('enter denomenator\n'))
        res = num/den
        print(res)
    except ZeroDivisionError as e:
        print('exception handled in fun()')
        raise e # next statement not printed --> rerising the exception bcz : python raise the exception 
    finally:
        print('fun() finished normally')

def main():
    print('main() started excecution')
    try:
        fun()
    except:
        print('exception handled in main()')
    print('main() ended excecution')
main()

def fun(x):
    try:
        res = 100 / x
        print("inside try")
    except:
        print("inside except")
    else:
        print("inside else")
    finally:
        print("inside finally")
def main():
    x = int(input("Enter x: "))
    fun(x)
main()
    