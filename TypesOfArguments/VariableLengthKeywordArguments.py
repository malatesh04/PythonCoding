# Variable length keyword arguments --> also called Arbritary keyword argument

def collect_student_data(**data): #here '**' represent variable length along with keyword argument.
    print(data)
    print(type(data)) # output in key value pair
collect_student_data(name = "malatesh",age = 21, avg = 50.5, gender = "M")