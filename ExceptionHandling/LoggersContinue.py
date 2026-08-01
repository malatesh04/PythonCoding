import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR,filemode='w',format='%(levelname)s:%(name)s:%(asctime)s:%(msg)s')
# or
# logging.basicConfig(filename='log.txt',level=40)
def fun():
    lst = [0,20,30,40,50]
    d = {1:'c',2:'java',3:'python',4:'c++'}
    try:
        r = int(input('enter the rank of language\n'))
        print(d[r])
        num = int(input('enter the index of numerator\n'))
        den = int(input('enter the index of denomenator\n'))
        print(lst[num]/lst[den])
    except KeyError: #specific block
        print('Key does not exist')
    except IndexError:
        print('index out of range')
    except ZeroDivisionError:
        print('denomenator is zero')
    except:
        print('something issue happened...')
        logging.error('exception occured',exc_info=True)
def main():
    fun()
main()