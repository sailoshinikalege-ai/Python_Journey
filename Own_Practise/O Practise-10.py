'''
class Student:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks
  def display(self):
    print('Name:',self.name)
    print('Marks:',self.marks)

s1 = Student('Nikky',85)
s2 = Student('Rahul',78)
s1.display()
s2.display()


numbers = [10, 15, 20, 25, 30, 35]
e = lambda i : i %2 ==0 
b = filter (e,numbers)
print(list(b))
'''
