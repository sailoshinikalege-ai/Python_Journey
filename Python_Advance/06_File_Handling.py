'''
#working with respect to text file
f = open("sample.txt", "w")

f.write("Hello Python")

f.close()

f = open("sample.txt", "a")

f.write("\nI am learning Python")

f.close()

#Wap to creat a dictionary conisits of works with its count given



import csv

with open('employees.csv', 'w', newline='') as a:

    b = csv.writer(a)

    b.writerow(['name', 'class', 'marks'])

    b.writerows([
        ['Himanshu', 'bca', 56],
        ['Nikky', 'bca', 98]
    ])

f = open('student.txt','w')
f.write("Name: Nikky\n")
f.write("Course: BCA\n")
f.write("College: Indira Priyadarshini Govt Degree College for Women\n")
f.close()

f = open('student.txt','r')
data = f.read()
print(data)
f.close()


f = open('college.txt','w')
f.write('Iam a BCA Student \n')
f.write('Iam learning Python')
f.close()

f = open ('names.txt','w')
f.write('Nikky \n')
f.write('Baby \n')
f.write('Chethan \n')
f.write('Teju \n')
f.write('Karthik\n')

f=open('cities.txt','w')
f.writelines(['Tamilnadu\n','Hyderabad\n','Chennai\n','Kerala\n'])
'''
f=open('numbers.txt','w')
i = 0
while i <=3:
  num = int(input())
  f.write(num +'\n')
  i +=1
f.close()



