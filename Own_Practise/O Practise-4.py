'''
#Take a 3-digit number and check whether the first digit and last digit are equal.
n =  input("Enter the num:")
if n[0]== n[-1]:
    print('first and last digits are same')
else:
    print('Not same')


Take one character and determine whether it is:

uppercase alphabet
lowercase alphabet
digit
special character

Hint: Use ord().

st = input('enter a character:')
if ord(st)>=65 and ord(st)<=91:
    print(st,"IS A UPPER CASE")
elif ord(st)>=96 and ord(st)<=122:
    print(st,'IS A LOWER CASE')
elif st in '1234567890':
    print(st,'IS A DIGIT')
else:
    print("Special charcter")


Calculate electricity bill based on units:

0 -100       → ₹2/unit
101 -200     → ₹3/unit
201- 300     → ₹5/unit
Above 300   → ₹7/unit

n = int(input("ENTER THE UNITS YOU CONSUME:"))
if n>=0 and n<=100:
    print("YOUR ELECTRICITY BILL IS:",n*2)
    print("HERE WE ARE CHARGING ₹2/unit ")
elif n>=101 and n<=200:
    print("YOUR ELECTRICITY BILL IS:",n*3)
    print("HERE WE ARE CHARGING ₹3/unit ")
elif n>=201 and n<=300:
    print("YOUR ELECTRICITY BILL IS:",n*5)
    print("HERE WE ARE CHARGING ₹5/unit ")
else: 
    print("YOUR ELECTRICITY BILL IS:",n*7)
    print("HERE WE ARE CHARGING ₹7/unit as your units are abover 300")


Input:day, month, year
Check whether the given date is valid.

date = int(input("ENTER THE DATE:"))
month = int(input("ENTER THE MONTH:"))
year= int(input("ENTER THE YEAR:"))
if month <=12 and date>0:
 if month in (1,3,5,7,8,10,12):
        if date<=31:
            print("valid")
        else:
            print('invalid date')
 elif month in (4,6,9,11):
        if date<=30:
            print("valid")
        else:
            print("not valid")
 elif month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if date <=29:
                print('valid')
        else:
            if date <= 28:
                print("valid")
            else:
                print("invalid")


    
    

    

#Take three di""fferent numbers and print the middle value, without using sort().
a = int(input("enter a num:"))
b = int(input("enter b num:"))
c = int (input("enter c num:"))
great =0
if a < b<c or c<b<a:
    print("B is the second greatest")
elif b< a<c or c<a<b:
    print("A is the second greatest")
elif a < c<b or b<c<a:
    print("C is the second greatest")


ATM Withdrawal

Rules:

Amount must be a multiple of 100
Withdrawal amount must not exceed balance
Minimum balance after withdrawal = ₹500

bal = int(input("enter the balance :"))
amt = int(input("enter the withdrawal amount :"))
if amt % 100==0:
    if amt<bal:
        if bal - amt >= 500:
          print("Yes withdrawal is suscessful!")
        else:
           print("its decreasing the min balance")
    else:
       print("your withdrawal is exceeding the balance")
else:
   print("enter the amt")

s1 = int(input("enter the side 1"))
s2 = int(input("enter the side 2"))
s3 = int(input("enter the side 3"))
if s1 + s2 > s3:
  if s1 + s3 > s2:
      if s2 + s3 > s1:
         print("IT forms a triangle")
         
if s1 == s2== s3:
    print("IT WILL FORM A EQUILATERAL ")
elif (s1 == s2) > s3:
    print("IT WILL FORM ISOSCELES")
elif s1< s2<s3:
    print("IT WILL FORM SCALANE")
else:
    print('invalid')

'''

'''
for i in range(1,6):
    for j in range(1,6):
        if i == j:
          print('*',end= ' ') 
        else :
           print(' ',end=' ')    #end is used to print them in same line
    print()

for i in range(1,6):
    for j in range(1,6):
        if i <= j:
          print('*',end= ' ') 
        else :
           print(' ',end=' ')    #end is used to print them in same line
    print()

for i in range(1,6):
    for j in range(1,6):
        if i >= j:
          print('*',end= ' ') 
        else :
           print(' ',end=' ')    #end is used to print them in same line
    print()


n = int(input('Enter your age:'))
ch = input('INDIAN OR NOT:')
if ch == 'INDIAN' :
   if n >=18:
     print('You are Indian,eligible')
   else:
      print('Not 18')
else:
   print('Not eligible')
'''
for i in range(1,6):
    for j in range(1,6):
        if i == j:
          print('*',end= ' ') 
        else :
           print(' ',end=' ')    #end is used to print them in same line
    print()

n = int(input())



