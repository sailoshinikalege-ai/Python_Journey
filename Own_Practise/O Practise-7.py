'''
class Student :
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def display (self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Course:',self.course)

s1 = Student('Nikky',19,'BCA')
s1.display()


class Car:
    def __init__(self,brand,colour,price):
        self.brand = brand
        self.colour=colour
        self.price = price
    def display (self):
        print('Brand:',self.brand)
        print('Colour:',self.colour)
        print('Price:',self.price)

c1 = Car('BMW','BLACK','1.5CR')

c1.display()

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print('Employee Name:',self.name)
        print('Salary:',self.salary)
        print('Department:',self.department)

emp1 = Employee('Rahul','1.5lac','Data Scientist')
emp2 = Employee('Priya','2.5lac','Data Engineer')

emp1.display()
emp2.display() 

class BankAccount:

    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance
        self.deposit_amt = 0
        self.withdrawal_amt = 0

    def deposit(self, deposit_amt):
        self.deposit_amt = deposit_amt
        self.balance += deposit_amt

    def withdraw(self, withdrawal_amt):
        self.withdrawal_amt = withdrawal_amt
        self.balance -= withdrawal_amt

    def display(self):
        print('ACCOUNT HOLDER NAME:', self.acc_holder)
        print('CURRENT BALANCE:', self.balance)
        print('DEPOSIT AMOUNT:', self.deposit_amt)
        print('WITHDRAWAL AMOUNT:', self.withdrawal_amt)


a1 = BankAccount('NIKKY', 20000)

a1.deposit(10000)
a1.withdraw(5000)

a1.display()

class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def display (self):
        print('Brand Name:',self.brand)
        print('Model Name:',self.model)
        print('Price:',self.price)

c1 = Mobile('IPHONE','PRO MAX',120000)
c2 = Mobile('SAMSUNG','S24 ',96000)

c1.display()
c2.display()

class Rectangle:
    def __init__(self,lenght,breadth):
        self.lenght = lenght
        self.breadth = breadth
        

    def area(self):
        print(self.lenght*self.breadth)

    def display(self):
        print('Lenght:',self.lenght)
        print('Breadth:',self.breadth)

a1 = Rectangle(20,30)

a1.display()
a1.area()
        

class Calculator:

    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
c1 = Calculator()


print(c1.add(10,20))
print(c1.multiply(5,4))

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def get_result(self):
        if self.marks >=40 :
            return 'Pass'
        else:
            return 'Fail'
s1 = Student('Nikky',85)

print(s1.get_result())


class BankAccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def check_balance(self):
        return self.balance 

    def add_money(self,amount):
      self.balance = self.balance + amount
      return self.balance
    
a1 = BankAccount('Nikky',20000) 

print(a1.check_balance())
print(a1.add_money(5000))
print(a1.check_balance())

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
'''        

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