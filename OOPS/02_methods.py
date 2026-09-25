
'''

Create a class Car with the following:

1. Instance variables:
   - brand
   - model
   - price

2. Create a display() object method to print all details.

3. Create a change_price() object method to update the car price.

4. Create one object with:
   Brand = "Toyota"
   Model = "Fortuner"
   Price = 3500000

5. Display the details.

6. Change the price to 3800000.

7. Display the updated details.

Expected Output:

Toyota Fortuner 3500000
Toyota Fortuner 3800000 

class Car :
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
  

    def change_price(self,new_price):
       self.price = new_price

    def display(self):
        print('Brand:',self.brand)
        print('Model:',self.model)
        print('Price:',self.price)

c1 = Car('Toyota','Fortuner',3500000)
c1.change_price(3800000)

c1.display()

class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def change_marks (self,new_marks):
        self.marks = new_marks

    def display(self):
        print('Name:',self.name)
        print('Marks:',self.marks)

s1=Student('Nikky',92)

s1.display()
s1.change_marks(98)
s1.display()

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def change_salary(self,new_salary):
        self.salary = new_salary
    def change_department(self,new_department):
        self.department = new_department
    def display(self):
        print('Name:',self.name)
        print('Salary:',self.salary)
        print('Department:',self.department)

emp1 = Employee('Rahul',50000,'Python Developer')


emp1.display()
        
emp1.change_salary(60000)
emp1.change_department('Full stack developer')

emp1.display()

'''
        

        

        