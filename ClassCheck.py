class Person:
    school ='IIMB'
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello '+self.name)

p1 = Person('Shubh', 20)
p1.age = 35
print(p1.age)
print(p1.name)
print(p1.school)
Person.greet(p1)


#Inheritance

class Student(Person):
    def courses(self, college, subject, grade):
        self.college = college
        self.subject = subject
        self.grade = grade

student1 = Student('Shobhit', 32)
student1.courses("IIT Delhi", {'Math', 'Science', 'Physics'},'A')

print(student1.name, student1.age, student1.college, student1.subject,student1.grade)


#classmethod vs staticmethod

class Number():
    def __init__(self,value):
        self.value = value

    @classmethod
    def sum(cls, value1, value2):
        return cls(value1+value2)

    @staticmethod
    def multiply(value1, value2):
        return Number(value1 * value2)


    def divide(value1, value2):
        return Number(value1 / value2)

    def print(self):
        print("Number",self.value)


class Float(Number):

    def print(self):
        print("Float" , self.value)

    @staticmethod
    def multiply(value1, value2):
        return Number(value1 * value2)

    def divide(value1, value2):
        return Number(value1 / value2)

# Takes the Child Attributes
F1 = Float.sum(2,3)
F1.print()

# Takes the Parents Attributes
F2 = Float.multiply(5,6)
F2.print()

# Takes the Parents Attributes
F3 = Float.divide(6,3)
F3.print()






