class Contact:
    all_contacts = []
    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    def display(self):
        print(self.__dict__)
def main():
    c1 = Contact('Malatesh','malatesh@gmail.com')
    c2 = Contact('Atharva','atharva@gmail.com')
    # print(Contact.all_contacts)
    for i in Contact.all_contacts:
        i.display()
if __name__ == '__main__':
    main()
