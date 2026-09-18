
#WAP: Write a Python program to overload the + operator to add the prices of two shopping items. 

class Shopping:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price


p1 = Shopping(200)
p2 = Shopping(300)

print("Total Price:", p1 + p2)

'''
1. Public Access Specifier:
WAP to create a Student class with a public variable name and display the student's name outside the class.
'''

class Student:
    name = "Rahul"

s1 = Student()

print("Student Name:", s1.name)

'''
2. Protected Access Specifier:
WAP to create an Employee class with a protected variable salary and access it from a child class.
'''

class Employee:
    _salary = 30000


class Manager(Employee):
    def display(self):
        print("Salary:", self._salary)


m1 = Manager()

m1.display()


'''
3. Private Access Specifier:
WAP to create a BankAccount class with a private variable balance and display the balance using a public method. 

class BankAccount:
    __balance = 5000

    def display(self):
        print("Balance:", self.__balance)


b1 = BankAccount()

b1.display()
'''
#Syntax Method

class Demo:

    __a = 10
    b = 20

    def __init__(self, c, d):
        self.__c = c
        self.__d = d

    def __display(self):
        print(self.__c, self.__d)

    def ch_c(self, new):
        self.__c = new

    @classmethod
    def __disp(cls):
        print(cls.__a, cls.b)

    @staticmethod
    def msg():
        print('Private access specifiers')


user = Demo(10, 20)

user._Demo__display()

Demo._Demo__disp()

user._Demo__c = 50

user._Demo__display()

Demo.msg() 
'''
class Demo():
    __a = 10
    def __init__(self,c):
        self.__c ==c
    def __display(self):
        print(self.__c)

user = Demo(20)
print(Demo._Demo__a)
print(user._Demo__c)
user._Demo__display()
    
#GETTER & SETTER METHOD

class Def:
    __a =10
    __b =20
    def __init__(self,c,d):
        self.c =c
        self.d =d

    def getter(self):
        return self.__c,self.__d
    def setter (self,new):
        self.__c = new

'''
#Property Decorator


#ABSTRCTION

from abc import ABC,abstractmethod
class Cal(ABC):
    @abstractmethod
    def add(self,a,b):
    
        pass
    def sub (self,a,b):
        pass
class Cal_up(Cal):
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
ob = Cal_up()
ob.add(10,20)
ob.sub(50,40)
