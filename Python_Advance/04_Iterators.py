'''
l = [5,10,15,20]
i = iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

l = [10, 20, 30]
i = iter(l)

for i in l:
    print(i)

class Numbers:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 8:
            value = self.num
            self.num = self.num +1
            return value
        else:
            raise StopIteration

m = Numbers()
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))\
'''
fruits = ["apple", "banana", "mango"]
f = iter(fruits)
print(next(f))
print(next(f))
print(next(f))
print(next(f))  