'''
i =1
while i<=10:
    print(i)
    i =i+1


i = 10
while i>=1:
    print(i)
    i = i-1

i = 0
while i<=20:
    print(i)
    i=i+2

i = 1
while i<=20:
    print(i)
    i = i+2
    

n = int(input("Enter the num:"))

i =0
while i<=10:
    print(f'{n} * {i} = {n*i}')
    i = i+1



n = int(input("Enter the number: "))
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)

n = int(input("Enter a num:"))

i = 2
sum = 0

while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print(sum)


num = int(input("Enter digit: "))
count = 0

while num > 0:
    digit = num % 10
    count = count + 1
    num = num // 10

print(count)



sum = int(input("Enter the digit:"))
i =0

while sum >0:
    digit = sum%10
    i = i+ digit
    sum = sum//10
print(i)


num = int(input("enter the number:"))
rev = 0

while num>0:
    digit = num%10
    rev = rev*10 +digit
    num = num// 10

print(rev)

i = 1

while i<=50:
    if i %5 ==0:
        print(i,"Divisible by 5")
    i =i+1
   

num= int(input("Enter a num:"))

i =0

while num>0:
    digit = num%10
    if digit > i:
          i = digit

    num = num//10

print(i, "largest")
          
'''
n = int(input())
for i in range (1,n+1):
    print(i**2)