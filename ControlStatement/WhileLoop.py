# while loop --> loop keep repeating itself until it false.


lst = [10,20,30,40,50]
# make again and again to take value from lst
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])


# taking a list 

lst = [1,2,3,4,5]
i = 0  #mandatory in while loop initializing compalsary
while(i<5):
    print(lst[i])
    i+=1


# taking my name 

name = "MALATESH BASAVANNEPPA NEGALUR"
n = 0
while n<29:
    print(name[n])
    n=n+1;

# 2 multiplication 

number = [1,2,3,4,5,6,7,8,9,10]
i = 0;
while i<10:
    print(number[i]*2)
    i = i+1;

# using While loop 
balance = 15500;
min_balance = 500;
deposite = int(input("deposite amount --> "))
 
print("before balance :",balance)
while min_balance < balance:
    balance = balance - deposite
    print("After amounut -- >",balance)

# using for loop
balance = 15500;
min_balance = 500;
deposite = int(input("deposite amount --> "))
 
print("before balance :",balance)
for i in range(1,5):
    balance = balance - deposite
    print("After amounut -- >",balance)