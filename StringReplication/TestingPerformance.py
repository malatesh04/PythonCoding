# testing which is high or low performance in formate() function or f string

import timeit

# Measure execution time of .format()
print(timeit.timeit(stmt='"{0:.2f}".format(3.1416)', number=10000))

# Measure execution time of f-string
print(timeit.timeit(stmt='f"{3.1416:.2f}"', number=10000))

