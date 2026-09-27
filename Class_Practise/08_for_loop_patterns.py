'''               

for i in range(1,4):
    for j in range(1,4):
        print('*', end='')     #end is used to print them in same line
    print()

n = int(input('enter a number:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        print('*', end='')
    print()
'''
'''
*
**
***
****
*****


n =2
for i in range (1,n+1):
    for j in range(1,6):
        print('*',end='')
    print()

n =5
for i in range (1,n+1):
    for j in range(1,4):
        print('#',end='')
    print()

n =1
for i in range (1,n+1):
    for j in range(1,4):
       print('*',end='')
    print()

n = 6
for i in range(1, n+1):
    for j in range(1, i+1):
        if i == j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        if i>j :
            print('*', end='')
        else:
            print('@', end='')
    print()

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        if i==j :
            print('@', end='')
        else:
            print('*', end='')
    print()
'''
'''
####$
###$&
##$&&
#$&&&
$&&&&

n = int(input("enter a num:"))

for i in range (1,n+1):
    for j in range (1,n+1):
        if i +j == n+1:
            print('$', end='')
        elif i+j>n+1:
            print('&', end='')
        elif i+j<n+1:
            print('#', end='')
        else:
            print(' ')
    print()
'''
n = int(input("enter a num: "))

for i in range(1, n+1):

    for j in range(i, n+1):

        if i == 1 or j == i or j == n or 1>j:
            print('*', end=' ')
        else:
            print(' ', end=' ')


    print()

n = int(input("enter a num: "))

for i in range(1, n+1):

    for j in range(1, n+1):

        if i == 1 or j == i or j == n:
            print('*', end=' ')

        else:
            print(' ', end=' ')

    print()
                     