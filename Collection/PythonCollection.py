cloths = {'shirts':100,'pants':85,'blazer':35} 
ele = {'mobile':199,'computer':50,'AC':30}
food = {'chips':20,'milk':70,'egg':10}
inv = {**cloths,**ele,**food}
print(inv)
print(inv['milk'])
inv['shirts'] = 95
print(inv)
print(cloths)

# using ChainMap collection --> 

from collections import ChainMap
cloths = {'shirts':100,'pants':85,'blazer':35} 
ele = {'mobile':199,'computer':50,'AC':30}
food = {'chips':20,'milk':70,'egg':10}
inv = ChainMap(cloths,ele,food)
print(inv)
inv['shirts'] = 95
print(inv)
print(cloths)

# using counter find number of character apearing
from collections import Counter
s = 'malatesh'
c = Counter(s)
print(c)

s = 'a','b','c','a','b','c','a','b'
c = Counter(s)
print(c)

s = {'a','b','c','a','b','c','a','b'}
c = Counter(s)
print(c)

from collections import Counter
s = Counter(a=10,b=20)
print(s)

s = Counter(['a','b','c','a','b','c','a','b'])
print(list(s.elements()))
print(s.most_common(1))
print(s.most_common(2))
print(s.most_common(3))

c1 = Counter(a=3,b=2,c=1)
c2 = Counter(a=1,b=2,c=3)
print(c1+c2)
print(c1-c2)
print(c1|c2)
print(c1&c2)

# NAMEDTUPLES -->
from collections import namedtuple
S = namedtuple('student',('name','age','branch','percentage'))
s1 = S('malatesh',22,'ECE',85.7)
print(s1)
print(s1[0])
print(s1.name)

# DOUBLE ENDED QUEVE --> 
lst = [10,20,30]
lst.append(40) # here big O(1) constant time complexity
lst.insert(0,99) # here big O(n) n time complexity 
print(lst)

# now use DEQUE STRUCTURE --> 
from collections import deque
dq = deque([10,20,30])
dq.append(40)
dq.appendleft(99)
print(dq)