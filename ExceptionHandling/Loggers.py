# Logger --> piece of code which will be attaching in your code 

def sum_evan(lst):
    print('sum_evn() started excecution')
    sum = 0
    for i in lst:
        if i%2 == 0:
            sum = sum+i
    print('sum_even() end excecution')
    return sum
def main():
    print('main() started excecution')
    lst = list(map(int, input().split()))
    print('input taken from user')
    print('calling sum_even function')
    res = sum_evan(lst)
    print('result sum_even() calculated')
    print(res)
    print('main() finished excecution')
main()

''' 2 : INFO Logging '''
import logging
def sum_evan(lst):
    logging.info('sum_evn() started excecution')
    sum = 0
    for i in lst:
        if i%2 == 0:
            sum = sum+i
    logging.info('sum_even() end excecution')
    return sum
def main():
    logging.basicConfig(filename='log.txt',level=logging.INFO)
    logging.info('main() started excecution') 
    lst = list(map(int, input().split()))
    logging.info('input taken from user')
    print('calling sum_even function')
    res = sum_evan(lst)
    logging.info('result sum_even() calculated')
    print(res)
    logging.info('main() finished excecution')
main()

''' Levels of logging : 
1 -> DEBUG : 10 : store debugging related information in log life
2 -> INFO : 20 : used to trace the program(flow of control)
3 -> WARNING : 30 : store warning related information in log life
4 -> ERROR : 40 : exception related information is to be stored
5 -> CRITICAL : 50 : used to capture info which results in culture failuver of application
'''

''' 1 : DEBUG LOGGING '''
import logging
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def main():
    logging.basicConfig(filename='log.txt',level=logging.DEBUG)
    logging.basicConfig(filename='log.txt',level=logging.INFO)
    # or
    # logging.basicConfig(filename='log.txt',level=10)
    logging.info('main() started')
    a = int(input('enter a number\n'))
    b = int(input('enter b number\n'))
    logging.debug(f'a = {a}')
    logging.debug(f'b = {b}')
    res1 = add(a,b)
    logging.debug(f'res1 = {res1}')
    res2 = sub(a,b)
    logging.debug(f'res1 = {res1}')
    res3 = mul(a,b)
    logging.debug(f'res1 = {res1}')
    res4 = div(a,b)
    logging.debug(f'res1 = {res1}') 
    logging.info('main() ended')
main()

''' WARNING LOGGING '''
import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
def validate(num):
    if len(num) == 10:
        print('valid phone number')
    else:
        logging.warning('Invalid phone number')
        print('Invalid phone number')
def main():
    num = input('enter a number\n')
    validate(num)
main()

''' ERROR LEVEL '''
import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR,filemode='w')
def div():
    try:
        num = int(input('enter a numerator\n'))
        den = int(input('enter a denomenator\n'))
        q = num/den
        print(q)
    except:
        logging.error('exception occured',exc_info=True)
def main():
    div()
main()