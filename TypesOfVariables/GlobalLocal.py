# # global variable :
# # --> variables which are created outside of all functions in python script.

# # local variable :
# #  --> variable which created inside the function.

# x = 99    # --> global variable/scope
# def function():
#     y = 999   # --> local variable/scope
#     print(y)
#     print(globals())
#     print(locals())
  
# # print(y)  they telling y not defined because y is created inside the function. 
# function()

x = 99
def fun():
    global x
    x = 999
    print(x)
fun()
print(x)