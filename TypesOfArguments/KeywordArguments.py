# in keyword argument we don't follow positional argumnets instead
# using keywords like whatever you define in parameter name give 
# it is a keyword

def power_of(a,b):
    c = a**b
    print(c)
power_of(a=2,b=5) 
power_of(b=5,a=2) # interchanging but same answer