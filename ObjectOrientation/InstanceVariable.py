# PROGRAM 01 -->

class Cricket:
    def __init__(self):
        self.name = 'malatesh'
        self.team = 'csk'
        self.run = 200
    def batting(self):
        print(self.name,'is batting now...')
    def bouling(self):
        print(self.name,'is bouling now...')
    def fieldng(self):
        print(self.name,'is fielding now...')

def main():
    c = Cricket()
    print(c.name)
    print(c.team)
    print(c.run)
    c.batting()
    c.bouling()
    c.fieldng()

if __name__ == '__main__':
    main()

# PROGRAM 02 --> one class multiple object

class FootBaller:
    def __init__(self,name,team,goals):
        self.name = name #states 
        self.team = team #states
        self.goals = goals #states
    def shotting(self):
        print(self.name,'shotting...') 
    def passing(self):
        print(self.name,'passing...')
    def running(self):
        print(self.name,'running...')

def main():
    f = FootBaller('messi','argentina',2)
    print(f.name)
    print(f.team)
    print(f.goals)
    f.shotting()
    f.passing()
    f.running()

    f2 = FootBaller('Ronaldo','Spanish',3)
    print(f.name)
    print(f.team)
    print(f.goals)
    f2.shotting()
    f2.passing()
    f2.running()

if __name__ == '__main()':
    main()


# PROGRAM 03 --> same as previous but you def function stored all state of object

class FootBaller:
    def __init__(self,name,team,goals):
        self.name = name #states 
        self.team = team #states
        self.goals = goals #states
    def shotting(self):
        print(self.name,'shotting...') 
    def passing(self):
        print(self.name,'passing...')
    def running(self):
        print(self.name,'running...')
    def Display(self):
        print(self.name)
        print(self.team)
        print(self.goals)

def main():
    f = FootBaller('messi','argentina',2)
    f.Display()
    f.shotting()
    f.passing()
    f.running()

    f2 = FootBaller('Ronaldo','Spanish',3)
    f2.Display()
    f2.shotting()
    f2.passing()
    f2.running()

if __name__ == '__main()':
    main()

# NOTES -->
# 1 --> __new__ --> this dunder is constuct the memory in stack
# 2 --> __init__ --> this dunder is goes under memory initialize the object


# PROGRAM 04 --> after creating object then you extra add new variables

class Cricket:
    def __init__(self):
        self.name = 'malatesh'
        self.team = 'csk'
        self.run = 200
    def batting(self):
        print(self.name,'is batting now...')
    def bouling(self):
        print(self.name,'is bouling now...')
    def fieldng(self):
        print(self.name,'is fielding now...')
    def display(self):
        print(self.name)
        print(self.team)
        print(self.run)
        print(self.age)
        print(self.jercy_no)

def main():
    c = Cricket()
    c.age = 44
    c.jercy_no = 7
    c.display()
    c.batting()
    c.bouling()
    c.fieldng()

if __name__ == '__main__':
    main()

# PROGRAM 05 --> after creating object then you extra add new variables using 'setattr

class Cricket:
    def __init__(self):
        self.name = 'malatesh'
        self.team = 'csk'
        self.run = 200
    def batting(self):
        print(self.name,'is batting now...')
    def bouling(self):
        print(self.name,'is bouling now...')
    def fieldng(self):
        print(self.name,'is fielding now...')
    def display(self):
        print(self.name)
        print(self.team)
        print(self.run)
        print(self.age)
        print(self.jercy_no)

def main():
    c = Cricket()
    setattr(c, 'age', 44)
    setattr(c, 'jercy_no', 7) # add new variable
    print(getattr(c, 'name')) # print name using getattr
    print(hasattr(c,'name')) # check name varable present or not if present gives true else false
    print(hasattr(c,'gender'))
    print(c.__dict__)

    c.display()
    c.batting()
    c.bouling()
    c.fieldng()

if __name__ == '__main__':
    main()