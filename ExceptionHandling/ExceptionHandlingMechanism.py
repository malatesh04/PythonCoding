'''inside fun2() added try and exception handler'''
def fun2():
    print('fun2() started execution')
    try:
        num = int(input('enter the numerator\n'))
        den = int(input('enter the denominator\n'))
        res = num/den
        print(res)
    except ZeroDivisionError:
        print('Exception handeled fun2()')
    print('fun2() ended normally')
def fun1():
    print('fun1() started execution')
    fun2()
    print('fun2() ended normally')
def main():
    print('main() started execution')
    fun1()
    print('main() ended normally')
main()

'''inside fun1() added try and exception handler'''
def fun2():
    print('fun2() started execution')
    num = int(input('enter the numerator\n'))
    den = int(input('enter the denominator\n'))
    res = num/den
    print(res)
    print('fun2() ended normally')
def fun1():
    print('fun1() started execution')
    try:
        fun2()
    except ZeroDivisionError:
        print('Exception handeled fun2()')
    print('fun2() ended normally')
def main():
    print('main() started execution')
    fun1()
    print('main() ended normally')
main()

'''inside main() added try and exception handler'''
def fun2():
    print('fun2() started execution')
    num = int(input('enter the numerator\n'))
    den = int(input('enter the denominator\n'))
    res = num/den
    print(res)
    print('fun2() ended normally')
def fun1():
    print('fun1() started execution')
    fun2()
    print('fun2() ended normally')
def main():
    print('main() started execution')
    try:
        fun1()
    except ZeroDivisionError:
        print('Exception handeled fun2()')
    print('main() ended normally')
main()