'''for i in range(1,11):
    print(i)

for i in range (2,21,2):
    print(i)

for i in range (3,21,3):
    print(i)

i =1
while i<=10:
    print(i)
    i = i+1

for i in range(1,11):
    if i ==6:
            break
    print(i)
   
for i in range(1,11):
    if i ==5:
        continue
    print(i)

for i in range (2,21):
    if i % 2==0:
        print(i)

sum =0
for i in range (1,11):
    sum = sum +i
print(sum)
 
a = int(input('Enter a num:'))
mul = 1

for i in range (1,11):
    mul = a*i
    print(mul)

num = int(input('Enter a number:'))

if num %2 ==0:
    print('Even')
else:
    print('Odd')
    
n = int(input('enter a number:'))
fac = 1
for i in range (1,n+1):
    fac = fac *i
print(fac)


fruits = ["apple", "banana", "mango"]
fruits.append('oranges')
fruits.insert(1,'grapes')
fruits.remove('banana')
print(len(fruits))
print(fruits)

numbers = [10, 25, 30, 45, 50, 65]

for i in numbers:
    if i >40:
        print(i)

ch = input('enter a string:')
count=0
for i in ch :
     count = count+1
print('lenght:',count)


ch = input('Enter a String:')

count = 0

for i in ch:
    if i in 'AEIOUaeiou':
        count = count + 1

print("Number of Vowels:", count)

ch = input('Enter a String:')

count = 0

for i in ch:
    if i not in 'AEIOUaeiou':
        count = count + 1

print("Number of Vowels:", count)

ch = input('Input:')
print(ch[::-1])

ch = input('Input:')
if ch[::1] == ch[::-1]:
  print('palindrome')

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1,15)
numbers.remove(30)
numbers.pop()
print(numbers)


student = {"name": "Sai", "age": 20, "course": "BCA"}
print(student["name"])
print(student["age"])

student.values('city':'hyderabad')

student = {"name": "Sai", "age": 20, "course": "BCA"}
print(student.keys())
print(student.values())

for i in student:
    if i == 'age':
        print('exist')


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)
print(b - a)

def greet():
    print('Hello, welcome to Python!')
greet()

def add (a,b):
    return a+b
add(10,20)

def greet(name="Sai"):
    print("Hello", name)

greet()
greet("Rahul")

def square(n):
    return n * n

result = square(5)
print(result)

numbers = [20, 60, 45, 80, 30, 100]

for i in numbers:
    if i > 50:
        print(i)

num = int(input('Enter the Num:'))
if num >0:
    if num >100:
        print('Positive and greater than 100')
    else:
        print('Positive but not greater than 100')
else:
    print('Not positive')


age = int(input('enter the age:'))
citizenship = input("Citizenship:")


if age >=18:
    if citizenship =='Indian':
     print("Eligible to vote")
    else:
     print('Not eligible - citizenship')
else:
    print('Not eligible - underage')

'''

user = input('Username:')
psw = int(input('Password:'))

if user == 'admin':
    if psw == 1234:
        print('login successful')
    else:
        print('incorrect password')
else:
    print('unvalid username')

