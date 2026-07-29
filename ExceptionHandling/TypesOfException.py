'''normal excecution not happens when logical error'''
print('excecution started normally')
lst = [10,20,0,40,50]
d = {1:'c',2:'java',3:'python',4:'c++'}
r = int(input('enter the rank of the language\n'))
print(d[r])
num = int(input('enter the index of numerator\n'))
den = int(input('enter the index of denomenator\n'))
print(lst[num]/lst[den])
print('excecution ended normally')

# exception handling-->
'''normal excecution happens when even logical error happens because exception handle it'''
'''but in this code when user '''
print('excecution started normally')
try:
    lst = [10,20,0,40,50]
    d = {1:'c',2:'java',3:'python',4:'c++'}
    r = int(input('enter the rank of the language\n'))
    print(d[r])
    num = int(input('enter the index of numerator\n'))
    den = int(input('enter the index of denomenator\n'))
except:
    print('give proper valid input')
else:
    print(lst[num]/lst[den])
print('excecution ended normally')

# one Try block multiple except 
print('excecution started normally')
try:
    lst = [10,20,0,40,50]
    d = {1:'c',2:'java',3:'python',4:'c++'}
    r = int(input('enter the rank of the language\n'))
    print(d[r])
    num = int(input('enter the index of numerator\n'))
    den = int(input('enter the index of denomenator\n'))
    print(lst[num]/lst[den])
except KeyError: # specific handler --> capable to handle specific error
    print('key does not exist')
except IndexError:  # specific handler
    print('index out of bound')
except ZeroDivisionError:  # specific handler
    print('divisible by zero')
except: # this block is taking exception from exception object
    print('value error')
print('excecution ended normally')

# one Try block multiple except 
print('excecution started normally')
try:
    lst = [10,20,0,40,50]
    d = {1:'c',2:'java',3:'python',4:'c++'}
    r = int(input('enter the rank of the language\n'))
    print(d[r])
    num = int(input('enter the index of numerator\n'))
    den = int(input('enter the index of denomenator\n'))
    print(lst[num]/lst[den])
except KeyError as e: # specific handler --> capable to handle specific error
    print(e)
except IndexError as e:  # specific handler
    print(e)
except ZeroDivisionError as e:  # specific handler
    print(e)
except Exception: # this block is taking exception from exception object
    print('value error')
print('excecution ended normally')