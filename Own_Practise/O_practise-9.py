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
'''
class Student:
    def __init__(self,marks):
        self.__marks = marks
    def display(self):
        print(self.__marks)
s1 = Student(85)
s1.display()
        