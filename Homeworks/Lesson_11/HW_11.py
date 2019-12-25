class Person():
    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

class Teacher (Person):
    def __init__(self, name, surname, gender, age,
                 salary, discipline, bribetaker):
        super().__init__(name, surname, gender, age)
        self.salary = salary
        self.discipline = discipline
        self.bribetaker = bribetaker
        self.info = [name, surname, gender, age,
                     salary, discipline, bribetaker]
    def __str__(self):
        return str(self.info)

class Student (Person):
    def __init__(self, name, surname, gender, age,
                 grant, course, average_mark):
        super().__init__(name, surname, gender, age)
        self.grant = grant
        self.course = course
        self.average_mark = average_mark
        self.student_info = [name, surname, gender, age,
                             grant, course, average_mark]
    def __str__(self):
        return str(self.student_info)

math_teacher = Teacher ('Olga', 'Petrova', 'Female', 42,
                        'Minimum', 'Math', 'Absolutely not!')
newbie_student = Student ('Oleg', 'Plyushkin', 'Male', 17, 'No', 1, 'C')

print (math_teacher)
print (newbie_student)

teacher1 = Teacher (input ('Please insert your name: '),
                    input ('Please insert your surname: '),
                    input ('Please insert your gender like "M" or "F": '),
                    input ('Please insert your age with the digits: '),
                    input ('Please insert your salary: '),
                    input ('Please insert what discipline do you teach: '),
                    input ('Anawer please, are you bribetaker? '))

print (teacher1)

student1 = Student (input ('Please insert your name: '),
                    input ('Please insert your surname: '),
                    input ('Please insert your gender like "M" or "F": '),
                    input ('Please insert your age with the digits: '),
                    input ('Please answer, have you a grant? '),
                    input ('Please insert your course: '),
                    input ('Anawer please, are you school average mark: '))

print (student1)
