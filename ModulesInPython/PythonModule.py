# using module name itself while calling function
import mymodule
mymodule.add()
mymodule.sub()
mymodule.mul()

# as used to change the imported name use 'as'
import mymodule as mm 
mm.add()
mm.sub()
mm.mul()

# using 'from' keyword 
from mymodule import *
add()
sub()
mul()

# use only specific function
from mymodule import add, sub, mul
add()
sub()
mul()


# here it tells what i created function i added description on 
# function whenever used help they give what were i put inside 
# the desctipion line
import mymodule
print(help(mymodule.add))
print(help(mymodule.sub))
print(help(mymodule))
print(mymodule.add__doc__)