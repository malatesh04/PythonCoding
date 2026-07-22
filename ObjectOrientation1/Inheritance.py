'''
INHERITANCE --> 

# DEFINITION --> 
1)is a oops concept where one class gets the properties(variables) and methods(functions) of another function.
2)is the process of creating a new class from an existing class .

# ADVANTAGE --> 
1) code reusability
2)reduce development time
3)easy maintainability

# TYPES OF INHERITANCE -->
1)SINGLE
2)MULTILEVEL
3)MULTIPLE
'''

# 1 --> single inheritance :

class Alpha:
    def func(self):
        print('Alpha class function()')
class Beta(Alpha):
    pass

b = Beta()
b.func()

# below only one class is there but they inherited by object 
class Alpha(object):
    def fun(self):
        print('single')
print(dir(Alpha))


# 2 --> MULTI LEVEL inheritance :
class Alpha:
    def fun1(self):
        print('Inside Alpha fun1()')
class Beta(Alpha):
    def fun2(self):
        print('Inside Beta fun2()')
class Gamma(Beta):
    pass
g = Gamma()
g.fun1()
g.fun2()
print(dir(Gamma))

# MULTIPLE INHERITANCE ->
class Alpha:
    def fun1(self):
        print('inside Alpha class fun1()')
class Beta:
    def fun2(self):
        print('inside Beta class fun2()')
class Gamma(Alpha,Beta):
    pass
g = Gamma()
g.fun1()
g.fun2()
print(dir(Gamma))

'''
ambiguity problem : When a child class inherits from multiple parent classes that contain methods 
with the same name, Python faces ambiguity about which method to execute. Python resolves this using 
the Method Resolution Order (MRO).
'''

class Alpha:
    def fun1(self):
        print('Aplha fun1()')
class Beta:
    def fun1(self):
        print('Beta fun1()')
class Gamma(Alpha,Beta):
    pass
g = Gamma()
g.fun1()
help(Gamma) 
print(Gamma.__mro__)
print(Gamma.mro()) # check the order 

# # METHOD RESOLUTION ORDER(MRO) : C3 LINEAR ALGORITHM.
'''
L(Alpha) --> Alpha object
L(Beta) --> Beta object
L(Gamma) --> Gamma + merge(L(Alpha), L(Beta), List of parents list) : 
L(Gamma) --> Gamma + merge(Alpha object, Beta object, AlphaBeta) : 

'''

class A:
    def fun(self):
        print('A')
class B:
    def fun(self):
        print('B')
class C:
    def fun(self):
        print('C')
class D:
    def fun(self):
        print('D')
class E(A,B):
    def fun(self):
        print('E')
class F(C,D):
    def fun(self):
        print('F')
class G(E,F):
    def fun(self):
        print('F')

a = G()
help(G) # to find the order.