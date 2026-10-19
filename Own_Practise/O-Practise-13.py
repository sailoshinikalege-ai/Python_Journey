'''
a = int(input('Enter a num:'))
b = int(input('Enter b num:'))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter the third number:'))

if a >=b and a>=c:
    print('Largest number is ',a)
elif b >=a and b>=c:
    print('Largest number is ',b)
else:
    print('Largest number is ',c)

for i in range(2,21,2):
    print(i)

numbers = [12, 7, 8, 15, 20, 3, 6]
count =0
for i in numbers:
    if i %2 ==0:
        count +=1
print('Number of even numbers:',count)


text = "Python Programming"
count = 0
for i in text:
    if i in 'AEIOUaeiou':
        count += 1
print('Number of vowels:',count)

numbers = [10, 20, 30, 40, 50]
sum =0
for i in numbers:
    sum += i
print('Total sum:',sum)

student = {
    'name': 'Nikky',
    'marks': 85,
    'age': 19
}


for key, value in student.items():
    print(f"{key}: {value}")

def calculate_square(a):
    return a**2
print(calculate_square(5))

def check_balance(bal):
    if bal>0:
        return 'Positive balance'
    elif bal==0:
        return 'Zero Balance'
    else:
        return'Negative Balanace'
print(check_balance(1000))
print(check_balance(0))
print(check_balance(-500))

a = [10, 20, 30]
b = a.copy()

b.append(40)

print(a)
print(b)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

def change_list(items):
    items.append(100)

numbers = [10, 20, 30]

change_list(numbers)

print(numbers)
x = 10

def show():
    x = 20
    print(x)

show()
print(x)

x = 10

def change():
    global x
    x = 20

change()
print(x)

numbers = [10, 10, 8, 8, 5, 3]
largest = 0
second = 0
for i in set(numbers):
    if i >largest:
        second = largest
        largest = i
    elif i> second:
        second=i
print(second)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in numbers:
    if i % 2 ==0 and i % 3 ==0:
        count +=1
print(count)

numbers = [1, 2, 3, 4, 5, 6]
result =[]
for i in numbers:
    if i %2 ==0:
        result.append(i**2)
print(result)

students = {
    "Anu": 85,
    "Ravi": 92,
    "Priya": 78,
    "Kiran": 92,
    "Sneha": 88
}

largest = 0

for name, score in students.items():
    if score > largest:
        largest = score

for name, score in students.items():
    if score == largest:
        print(name)

'''
users = {
    "nikky": "python123",
    "ravi": "hello456",
    "anu": "welcome789"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if password == users[username]:
        print("Login successful")
    elif password != users[username]:
        
    else:
        print("Incorrect password")
else:
    print("User not found")

