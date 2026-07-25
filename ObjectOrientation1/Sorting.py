lst = [27,54,9,24,89,97,67,89,98]
print(lst)
lst.sort()
print(lst)

# In reverse :
lst = [27,54,9,24,89,97,67,89,98]
lst.sort(reverse=True)
print(lst)

lst = ['python','java','c','go','c#']
print(lst)
lst.sort()
print(lst)

# reverse
lst = ['python','java','c','go','c#']
print(lst)
lst.sort(reverse=True)
print(lst)

lst = ['python',30,10,'java',57,'c','go','c#']
print(lst)
lst.sort(reverse=True) # sorting happens only homogenius data
print(lst)

# SELECTION SORT :
lst = [10,2,30,40,23]
for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[j] < lst[i]:
            lst[i],lst[j] = lst[j],lst[i]
print(lst)

# APPLY SELECTION SORT USER DEFINED OBJECT :
class Footballer:
    def __init__(self,name,goals,assist):
        self.name = name
        self.goals = goals
        self.assist = assist
    def display(self):
        print(self.__dict__)
    def __lt__(self, other):   # giving dunder lesser than magic method
        if self.goals < other.goals:
            return True
        else:
            return False
    def __gt__(self, other): # giving dunder greter than magic method
        if self.goals > other.goals:
            return True
        else:
            return False
def main():
    f1 = Footballer('messi',600,300) # 1st footballer object
    f2 = Footballer('ronaldo',500,200) # 2nd footballer object
    f1.display()
    f2.display()
    print(f1<f2) # internally -->> print(f1.__lt__(f2))
    print(f2<f1) # internally -->> print(f2.__lt__(f1))
    print(f1>f2) # internally -->> print(f1.__gt__(f2))
    print(f2>f1) # internally -->> print(f2.__gt__(f1))  
main()

class Footballer:
    def __init__(self,name,goals,assist):
        self.name = name
        self.goals = goals
        self.assist = assist
    def __lt__(self, other):   # giving dunder lesser than magic method
        self.goals < other.goals
    def __gt__(self, other): # giving dunder greter than magic method
        self.goals > other.goals
    def __str__(self):
        return f'{self.name}{self.goals}{self.assist}'
def sort_footballer(lst):
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
                lst[i],lst[j] = lst[j],lst[i]
def main():
    f1 = Footballer('messi',650,359)
    f2 = Footballer('ronaldo',750,250)
    f3 = Footballer('luis',300,600)
    f4 = Footballer('neymer',450,125)
    l = [f1,f2,f3,f4]
    sort_footballer(l)
    for i in l:
        print(i)
main()

class Footballer:
    def __init__(self,name,goals,assist):
        self.name = name
        self.goals = goals
        self.assist = assist
    def __lt__(self, other):   # giving dunder lesser than magic method
        return self.goals < other.goals
    def __gt__(self, other): # giving dunder greter than magic method
        return self.goals > other.goals
    def __str__(self):
        return f'{self.name}{self.goals}{self.assist}'
def main():
    f1 = Footballer('messi',650,359)
    f2 = Footballer('ronaldo',750,250)
    f3 = Footballer('luis',300,600)
    f4 = Footballer('neymer',450,125)
    lst = [f1,f2,f3,f4]
    lst.sort()
    for i in lst:
        print(i)
main()