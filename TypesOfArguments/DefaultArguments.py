# Default Argument --> also called Optional Arguments
#here i compulsary to give 2 arguments else error apears
# Now overcome this give default value b is 0

def power_of(a,b):
    c = a ** b
    print(c)
power_of(2)  #error apears


def power_of(a,b=0): #here i give defualt value 
    c = a ** b
    print(c)
power_of(2)
power_of(2,5)
power_of()

# situvation --> hing kottaga yavaga non default argument ystara 
# kodu but when you give default value to one parameter then next 
# parameter also be default parameter else they give error
def power_of(a,b=10):
    print(a,b)
power_of(2)

# --> see
def power_of(a,b=10,c):
    print(a,b,c)
power_of(2,3,4)  # hinga kodaka baralla

#  --> see
def power_of(a,b=1,c=2):
    print(a,b,c)
power_of(2,3,4) 
#omme defalut value kott mele next default kodbahudu but 
# non default value kodaka baraalla



 