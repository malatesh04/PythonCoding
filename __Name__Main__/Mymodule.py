def power_of(a,b):
    '''This function calculate power of number'''
    pow = a**b
    print(pow)

def get_quotiont(p,q):
    '''This function calculate quotiont of number'''
    res = p/q
    print(res)


if __name__=='__main__':
    power_of(2,5)
    get_quotiont(100,5)

# OR 

def main(): # yella call function main function daga haki adna if condition daggu hakbahudu run in terminal
    power_of(2,5)
    get_quotiont(100,5)

if __name__=='__main__':
    main()



# if __name__=='__main__': --> because :
# if dunder name is equal to dunder main they will check
# --> why they check : just to see whether file excecuting as 
# script of it is been imported as a module only if it is excecuted 
# as a script if line condition work but it is executed as module 
# never ever those call function excecute.