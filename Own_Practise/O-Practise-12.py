'''
numbers = [3, 8, 5, 12, 7, 10]
result = [ ]
for i in numbers:
    if i %2 == 0:
     result.append(i)
print(result)

numbers = [2, 5, 8, 3, 10, 7, 12]
result = [ ]
for i in numbers:
    if i %2 == 0:
     result.append(i**2)
print(result)

numbers = [12, 7, 20, 3, 15, 8, 25, 10]
result = [ ]
for i in numbers:
    if i>10:
     result.append(i)
print(result)

words = ["apple", "cat", "banana", "dog", "mango", "hi"]
result =[ ]
for i in words:
    if len(i)>4:
        result.append(i)
print(result)

numbers = [4, 7, 12, 15, 20, 23, 30, 9]
result = [ ]
for i in numbers:
    if i >10 and i% 5==0:
        result.append(i)
print(result)

numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26]
result = [ ]
for i in numbers:
    if i %2 ==0 and i % 4 != 0:
        result.append(i)
print(result)

numbers = [12, 5, 8, 21, 16, 7, 30, 9]
result = []
for i in numbers:
    if i >10:
        result.append(i**2)
print(result)

numbers = [12, 5, 8, 21, 16, 7, 30, 9]
count = 0
for i in numbers:
    if i > 10:
        count = count +1
print(count)

numbers = [3, 8, 12, 5, 7, 10, 14, 9]
count = 0
for i in numbers:
    if i % 2==0:
        count+=1
print(count)

words = ["apple", "cat", "banana", "dog", "mango", "hi"]
count = 0 
for i in words:
    if len (i)<=5:
        count +=1
print(count)

numbers = [2, 4, 2, 6, 4, 8, 6, 10]
result = []
for i in numbers:
    if i not in result:
        result.append(i)
        
print(result)

numbers = [10, 25, 8, 40, 15, 30]
largest = max (numbers)
numbers.remove(largest)
second = max(numbers)
print(second)

numbers = [18, 5, 27, 3, 14, 9, 22]
smallest = min(numbers)
numbers.remove(smallest)
second = min(numbers)
print(second)

numbers = [12, 45, 7, 30, 25, 50, 18]
largest=0
second = 0
third = 0
for i in numbers:
    if i > largest:
       third = second
       second = largest
       largest = i
       
    elif i > second:
          third = second
          second=i
          
    elif i > third:
           third = i

print(third)

numbers = [15, 8, 42, 23, 36, 10,42]
largest = 0
second =0
for i in numbers:
     if i > largest:
          second = largest
          largest = i
     elif i <largest and i >second:
          second = i
print(second)
'''
numbers = [2, 3, 2, 5, 3, 2, 8, 5]
result = 0

for i in set(numbers):
    print(i,'appers',numbers.count(i),'times')
   
   