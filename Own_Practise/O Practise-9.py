'''
class Student:
    name = 'Nikky'
    roll_no = 23
c1 = Student()
c2 = Student()
print(c1.name,c1.roll_no)
print(c2.name,c2.roll_no)


class Student :
    def __init__(self,name, roll_no,marks):
      self.name = name
      self.roll_no = roll_no
      self.marks = marks
    def display(self):
       print(self.name,self.roll_no,self.marks)
s1 = Student('Nikky',23,85)
s2 = Student('Rahul',24,78)

s1.display()
s2.display()


class Employee:
    def __init__(self,name,salary,bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus
    def display(self):
        print('Name:',self.name)
        print('Salary:',self.salary)
        print('Bonus:',self.bonus)
    def total_salary(self):
      
        print(self.name,self.salary + self.bonus)
emp1 = Employee('Nikky',25000,5000)

emp1.display()
emp1.total_salary()

class BankAccount:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display(self):
        print('ACCOUNT HOLDER:', self.acc_holder)
        print('CURRENT BALANCE:', self.balance)


a1 = BankAccount('Nikky', 10000)

a1.deposit(2000)
a1.withdraw(3000)

a1.display()

class Animal:
    def eat(self):
        print('Animal eats')
class Dog(Animal):
    def bark(self):
        print('Dof barks')
dog = Dog()
dog.eat()
dog.bark()

class Animal:
    def sound(self):
        print('Animal makes sound')
class Dog(Animal):
    def sound(self):
        print('Dog barks')
dog = Dog()
dog.sound()

class Father:
    def skills(self):
        print('Driving')
class Mother:
    def hobby(self):
        print('Cooking')
class Child(Father,Mother):
        pass
c1 = Child()
c1.skills()
c1.hobby()


class GrandFather:
    def house(self):
        print('Grandfather has a house')
class Father(GrandFather):
    def car(self):
        print('Father has a car')
class Son(Father):
    pass
s1 = Son()
s1.house()
s1.car()

class Animal:
    def eat(self):
        print('Animal eats')
class Dog(Animal):
    def bark(self):
        print('Dog barks')
class Cat(Animal):
    def meow(self):
        print('Cat meows')

d1 = Dog()
d1.bark()
c1 = Cat()
c1.meow()

class Student:
    def __init__(self,marks):
        self.__marks = marks
    def display(self):
        print(self.__marks)
s1 = Student(85)
s1.display()

class Student:
    def __init__(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks

s1 = Student(85)
print(s1.get_marks())

class Student:
    def __init__(self,marks):
            self.__marks = marks
    def set_marks(self,new_marks):
          self.__marks = new_marks
    def get_marks(self):
          return self.__marks
s1 = Student(85)
s1.set_marks(95)
print(s1.get_marks())

class Student:
    def __init__(self,marks):
        self.__marks = marks  
    def set_marks(self,new_marks):
        if new_marks >=0 and new_marks<=100:
         self.__marks = new_marks
        else:
           
           print('Invalid marks')
    def get_marks(self):
        return self.__marks         
s1 = Student(85)

print(s1.get_marks())
s1.set_marks(120)

class Student:
     def __init__(self,marks):
            self.__marks = marks 
s1 = Student(84)
print(s1._Student__marks)

class BankAccount:
      def __init__(self,balance):
            self.__balance = balance
b1 = BankAccount(5000)
print(b1._BankAccount__balance)

class Employee:
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        self.__salary = new_salary
emp1 = Employee(30000)
emp1.set_salary(35000)
print(emp1.get_salary())

from abc import ABC,abstractmethod
class Shape (ABC) :
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        lenght = 10
        breadth = 5
        print(lenght*breadth)

s1 = Rectangle()
s1.area()

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print('Car stars with key')

c1 = Car()
c1.start()

class Animal:
    def sound(self):
        print('Animals make sound')
class Dog(Animal):
    def sound(self):
        print('Dogs bark')
class Cat(Animal):
    def sound(self):
        print('Cat meows')

d1= Dog()
d1.sound()

c1=Cat()
c1.sound()

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount >=0 :
            self.__balance = amount
            print(amount)
        else:
            pass
a1 = BankAccount(10000)
a1.set_balance(15000)
''
class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, new_marks):
        if new_marks >= 0 and new_marks <= 100:
            self.__marks = new_marks
        else:
            print('Invalid marks')


s1 = Student(80)

s1.marks = 95

print(s1.marks)

def greet(func):

    def wrapper():
        print('Good morning')
        func()

    return wrapper


@greet
def display():
    print("Hello Nikky")


display()

def welcome(func):

    def wrapper():
        print("Welcome")
        func()

    return wrapper
@greet
def display():
    print('hello')
display()
'
def finish (func):

    def work():
     print('Working')
     func()

    return work
@finish
def display():
   print('Done')
display()

def study_time(func):
  print ('Start studying')

  def study():
    func()
    print("Studying Python")
  return study
@study_time
def display ():
  print('Finished studying')
display()

def welcome(func):
    
    def wrapper():
      print('Welcome')
      func()
    return wrapper
@welcome
def student():
   print('Nikky is studying')
student()

def login(func):

    def wrapper():
        print('CHECKING LOGIN')
        func()
    return wrapper
@login
def dashboard():
    print('Welcome to DashBoard')
dashboard()

def print_result(func):

    def wrapper():
        func()
        print('Thank you')
    return wrapper

@print_result
def calculate():
    print('Calculation completed')

calculate()

def security(func):

    def wrapper():
        print('checking security')
        func()
        print('Security check completed')
    return wrapper

@security
def account():
    print('Account opened')
account()


def welcome(func):
    def wrapper():
        print('Welcome Nikky')
        func()
        print('Keep Learning')
    return wrapper

@welcome
def student():
    print('Nikky is learning python')
student()

l = [5,10,15,20]
i = iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

l = [10, 20, 30]
i = iter(l)

for i in l:
    print(i)

'''
class Numbers:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 8:
            value = self.num
            self.num = self.num +1
            return value
        else:
            raise StopIteration

m = Numbers()
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))