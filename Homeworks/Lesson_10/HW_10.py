class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk (self):
        print ('Hello, my name is', self.firstname, self.lastname, "and I'm", self.age, 'years old')

my_person = Person ('Oleksandr', 'Bilozortsev', '30')
my_person.talk()
