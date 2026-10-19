#Genrator
'''
def sam():
    print('hellow')
    yield 1
    print('hi')
    yield 2
print(list (sam()))


def sq():
    yield 1**2
    yield 2**2
    yield 3**2
    yield 4**2
    yield 5**2
    yield 6**2
    yield 7**2
    yield 8**2
    yield 9**2
    yield 10**2

print(list(sq()))

#WAP TO EXTRACT ALL THE STRINGS FROM LIST COLLECTION ONLY IF IT IS PALINDROM

def pal():
    l = ['nayan','hii',7,9.7,6+4j,'aba','mom']
    for i in l:
      if type(i) == str:
        if i [::1]==i[::-1]:
            yield i
print(list(pal()))

#Wap to creat the following dictionary
#[a,65,b,66 ......]
def ch():
   
    for i in range(65, 91):
        yield chr(i ), i

print(dict(ch()))

#g = 'GenERat@r2'
# out = {G:g,e:E,......@:@,r:R,2:2}
def gen():
    g = 'GenERat@r2'

    for i in g:
        if i.upper() != i.lower():
            yield i.lower(), i.upper()
        else:
            yield i, i

print(dict(gen()))

def fruits():
    yield 'apple'
    yield 'banana'
    yield 'mango'

f = fruits()

print(next(f))
print(next(f))
print(next(f))

def numbers():
    for i in range (1,6):
        yield i

n = numbers()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

def even():
    for i in range (2,11,2):
        yield i
n = even()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))


def sq():
    for i in range (1,6):
        yield i**2
n = sq()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

def even ():
    for i in range (1,11):
        if i % 2==0:
            yield i
n = even()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))


def countdown():
    for i in range (5,0,-1):
        yield i
n = countdown()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

def multiples():
    for i in range (3,16,3):
        yield i
n = multiples()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

def cube():
    for i in range (1,6):
        yield i **3
n = cube()

for i in n :
    print(i)
'''
def pos(): 
 numbers = [-5, 10, -3, 7, 0, 15, -2, 8]
 for i in numbers:
    if i >0 :
      yield i
n = pos()
for i in n :
  print(i)
