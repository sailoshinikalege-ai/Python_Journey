#MAP FUNCTION used to consider a coll and it applies the same functionality to each and every value present in the collection
'''
SYNTAX:
var =map(fname.collection)
print(list(var))
'''
'''
#Wap to find the square of all the numbers from 1 to 10

a = lambda i:i**2
b = map(a,range(1,11))
print(list(b))

#Wap to add 10 to every number present in the list

# WAP to add 10 to every number present in the list

m = lambda j: j + 10
n = map(m, [10, 20, 30, 40])
print(list(n))

#Wap to find the cube of every number present in the list

l = lambda x:x**3
k = map(l,[1,2,3,4,5])
print(list(k))

#Wap to convert all the string to upper case

name = lambda f :f.upper()
g = map (name,['apple','orange','grape','litchi'])
print(list(g))

s = lambda n : n[0]+n[-1]
m = map(s,['hii','hello'])
print(list(m))

#get the following input
#g = ['abcd'],['start'],['data'],['python']
#output = [4,5,4,6]

g = lambda a:len(a)
n = map(g,['abcd','start','data','python'])
print(list(n))
'''
#get the following the output
#out ={1:1,2:8,.....}

power = lambda a: (a, a**3)
n = map(power, range(1, 6))
print(dict(n))

#get the following ouptpu
#s = 'programs on map function'
#out = {'programs':smasgorp}
rev = lambda a:(a,a[::-1])
n = map(rev,'programs on map function'.split())
print(dict(n))

#Filter func used to remove unwanted values present inside the collection

'''
Syntax:
var = filter(fname.collection)
print()
'''
#to extrct all the string values of tuple only if starts with upper and end with lower
#t = (10,2.3,'Apple','home','pythoN','Orange')

t = (10, 2.3, 'Apple', 'home', 'pythoN', 'Orange')
vowel = lambda a: str(a)[0].isupper() and str(a)[-1].islower()
b = filter(vowel, t)
print(list(b))


#prohgram to extract all the collection values present in a list which has even lenght
l = [10,2.3,'orange',[10,20,30],(7,8),{1,2,3,4}]
e = lambda i:len(i) % 2 !=0
a = filter(e,l)
print()
