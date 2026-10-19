m1= int(input('enter your marks:'))
m2= int(input('enter your marks:'))
m3= int(input('enter your marks:'))
m4= int(input('enter your marks:'))
m5= int(input('enter your marks:'))

total = m1+m2+m3+m4+m5
avg = total/5

if avg>=70:
    print('pass in distinction')
elif avg>=60 and avg<70:
    print('firstclass')
elif avg>35 and avg<60:
    print('second class')
else:
    print('fail')