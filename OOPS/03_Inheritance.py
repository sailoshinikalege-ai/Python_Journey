'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person(self):
        print('Name:',self.name)
        print('AGE:',self.age)

class Student (Person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course = course
    def display_student(self):
        print('Course:',self.course)

s1 = Student ('nikky',19,'BCA')
s1.display_person()
s1.display_student()
     

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person(self):
        print('Name:',self.name)
        print('Age:',self.age)

class Student(Person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course = course
    def display_student(self):
        print('Course:',self.course)

class CollegeStudent(Student):
    def __init__(self, name, age, course,college):
        super().__init__(name, age, course)
        self.college = college

    def display_college(self):
        print('College:',self.college)
cs1 = CollegeStudent('Nikky',19,'BCA','IPDGC')

cs1.display_person()
cs1.display_student()
cs1.display_college()

#Multi level inheritance
class Father:
    def __init__(self,father):
        self.father = father
    def father_name(self):
        print('Father name:',self.father)

class Mother:
     def __init__(self,mother):
            self.mother= mother
     def mother_name(self):
            print('Mother name:',self.mother)

class Child(Father,Mother):
      def __init__(self,father,mother,child):
            Father.__init__(self,father)
            Mother.__init__(self,mother)
            self.child =child
      def child_name(self):
             print('Child name:',self.child)

c1 = Child('SATYANARAYANA','ANITHA','NIKKY')
c1.father_name()
c1.mother_name()
c1.child_name()
'''
#HEIRACIAL 
class Animal:
    def __init__(self,name):
        self.name= name
    def display_name(self):
        print('Name:',self.name)
class Dog(Animal):
    def bark(self):
        print('It barks')
class Cat(Animal):
    def meow(self):
        print('It meows')

c1 = Cat('nikky')
d1 = Dog('Oreo')


c1.display_name()
c1.meow()

d1.display_name()
d1.bark()