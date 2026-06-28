# Command Line Promt -- > 
# inputs or arguments passed to a programm via command line even before excecution.
import sys
print(int(sys.argv[0]))
print(int(sys.argv[1]))
print(int(sys.argv[2]))

res = int(sys.argv[1]/sys.argv[2])
print(res)



# PRINT() --> Function
# syntax --> print(values(s), sep = '', end = '\n')
x=10
y=20
z=30
print(x, y, z)
print(x, y, z, sep='*', end='??' )
