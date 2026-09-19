#LAMBDA
#Its anonymous function, no func name

#Wap to print even 

even = lambda n: n %2 ==0
print(even(10))

#Wap to add two numbers

add = lambda a , b: a+b
print(add(2,3))

#Wap to find the square of a number

square = lambda n ,m :n**m
print(square(3,2))

#Wap a program to find cube of a number

cube = lambda c,d:c**d
print(cube(3,3))

#Wap to check whether the given string is starting with a vowel or not

vowel = lambda x : x[0] in 'AEIOUaeiou'
print(vowel('Happy'))

#Program to check whether the given value is present in a given list

check = lambda x : x in [1,2,3,4]
print(check(4))

#Wap to check whether a num is divisible by 6

div = lambda y : y % 6==0
print(div(36))

#Wap to multiply 2 number

mul = lambda a ,b : a*b
print(mul(2,3))



#Wap to find the remainder of two numbers

rem = lambda m , n : m%n
print(rem(3,2))

#WAp to find the largest value among three numbers

large = lambda x, y,z : max(x,y,z)
print(large(4,53,67))

# WAP to find the largest value among three numbers

large = lambda x, y, z: x if x > y and x > z else y if y > z else z

print(large(4, 53, 67))

#Wap to find the smallest value among 4 numbers

small = lambda a,b,c,d:min (a,b,c,d)
print(small(34,43,54,65))

#wwap to find the lenght of a given string

lenght = lambda m : len(m)
print(lenght('Nikky'))

#Program to check whether the given string is palindrome or if it is plaindrom the return the string as it is else retuen the reversed string

palin = lambda i: i if i[::1] == i[::-1] else i[::-1]

print(palin('mom'))


#program to add min two num and max 5 num.

add=lambda a,b,c=0,d=0,e=0:a+b+c+d+e
print(add(10,20))
print(add(1,2,3,4))

#program to return the concatenated lists if both has the same length else return the first list.

l=lambda l1,l2:l1+l2 if len(l1)==len(l2) else l1
print(l([1,2],[3,4]))
print(l([1,2,3],[4,5]))

#WAP TO CHECK WHETHER A NUM IS EVEN OR ODD.

check=lambda n:'even' if n%2==0 else 'odd'
print(check(10))

#Wap to return 'pass' if marks are 35 or above, otherwise retun 'Fail'

res=lambda marks:'pass' if marks>=35 else 'fail'
print(res(50))

#Wap to return the second num if two nums are equal, otherwise return their sum.

res=lambda a,b:b if a==b else a+b
print(res(10,10))
print(res(10,20))

#Wap to return the string in uppercase if its length is greater than 5, otherwise return it in lowercase.

res=lambda s:s.upper() if len(s)>5 else s.lower()
print(res('HELLO WORLD'))
print(res('HELLO'))

#program to return the list as it is if its length is even, otherwise return the reversed list.

res=lambda l:l if len(l)%2==0 else l[::-1]
print(res([1,2,3,4]))
print(res([1,2,3]))

#program to return the larger number if two nums are different, otherwise return their square.

res= lambda a,b: max(a,b) if a!=b else a*a
print(res(10,20))
print(res(10,10))

#program to return the sum of two numbers if both are even, otherwise return their product.

res=lambda a,b:a+b if a%2==0 and b%2==0 else a*b
print(res(10,20))
print(res(5,3))


