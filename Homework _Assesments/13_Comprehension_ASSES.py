# =========================================
#       PYTHON COMPREHENSION ASSESSMENT
# =========================================

# LIST COMPREHENSION (Q1–Q10)

# Syntax 1 : [value for var in collection if condition]

# Q1. WAP to create a list of squares of even numbers from 1–20.
 
l = [i for i in range (1,21) if i %2 ==0]
print(l)

# Q2. WAP to create a list of numbers divisible by 5 from 1–100.
n = [m for m in range (1,101) if m % 5 ==0]
print(n)

# Q3. WAP to create a list of positive numbers from a given list.
a = [i for i in [1,-2,3,-4,-6,7,8] if i >0]
print(a)

# Q4. WAP to create a list of vowels from a given string.
v = [k for k in 'Hello World' if k in 'AEIOUaeiou']
print(v)

# Syntax 2 : [TSB if condition else FSB for var in collection]

# Q5. WAP to replace each number with "Even" or "Odd" from 1–20.

k = ['Even' if l % 2 == 0 else 'Odd' for l in range(1,21)]
print(k)

# Q6. WAP to store "Pass" if marks are 35 or above, otherwise "Fail".

f = ['Pass' if i >=35 else 'Fail' for i in [13,58,98,23] ]
print(f)

# Q7. WAP to store "Adult" if age is 18 or above, otherwise "Minor".

m = ['Adult' if age >=18 else 'Minor' for age in [23,12,11,16]]

# Syntax 3 : [var1, var2 for var1 in col1 for var2 in col2]

# Q8. WAP to create all possible pairs of two lists.
a = [1, 2]
b = ['A', 'B']

p = [(i, j) for i in a for j in b]
print(p)


# Q9. WAP to create all combinations of colors and sizes.
a = ['Orange','Pink','Red']
b = [21 , 24 ,35]

p = [(i, j) for i in a for j in b]
print(p)

# Q10. WAP to create all combinations of students and subjects.
a = ['Ajay','Nikky','Pradeep']
b = ['BOTANY','DATASCIENCE','COMMERCE']

p = [(i, j) for i in a for j in b]
print(p)


# =========================================
#       SET COMPREHENSION (Q11–Q20)
# =========================================

# Syntax 1 : {value for var in collection if condition}

# Q11. WAP to create a set of square numbers from 1–15.
l = {i*i for i in range (1,16)}
print(l)

# Q12. WAP to create a set of unique even numbers from a list.
k = [12,34,21,27]
m = {n for n in k if n %2 ==0}
print(m)

# Q13. WAP to create a set of vowels from a string.
v = {k for k in 'HelloWorld' if k in 'AEIOUaeiou'}
print(v)

# Q14. WAP to create a set of numbers divisible by both 3 and 4.
d = {a for a in {12,34,67,68,45,34,36} if a % 3 ==0 and a %4 ==0}
print(d)

# Syntax 2 : {TSB if condition else FSB for var in collection}

# Q15. WAP to store "Positive" or "Negative" in a set.
s = {'Positive' if i >0 else 'Negative' for i in {23,-3,56,-4,-6,78,-6}}
print(s)

# Q16. WAP to store "Pass" or "Fail" from a list of marks.
m = {'Pass' if l >=35 else 'Fail' for l in {23,45,67,12,13,14}}
print(m)

# Q17. WAP to store "Long" or "Short" based on word length.
l = {'Long' if len(i) >= 5 else 'Short' for i in {'Python','luv','Nikky','Chemistry'}}
print(l)


# Syntax 3 : {var1, var2 for var1 in col1 for var2 in col2}

# Q18. WAP to create all ordered pairs from two sets.

a = {1,3,5,6,7}
b ={0,13,15,76,86}

l = {(i,j) for i in a for j in b }
print(l)

# Q19. WAP to create all combinations of fruits and drinks.
a = {'ORANGE','MUSKMELON','MANGO'}
b ={'PULPY','MUSKMELON JUICE','MAZZA'}

l = {(i,j) for i in a for j in b }
print(l)

# Q20. WAP to create all combinations of departments and employees.
a = {'BCA','BSC.HONS','BBA'}
b ={'NIKKY','LAKKY','ANITHA'}

l = {(i,j) for i in a for j in b }
print(l)

# =========================================
#   DICTIONARY COMPREHENSION (Q21–Q30)
# =========================================

# Syntax 1 : {key:value for var in collection if condition}

# Q21. WAP to create a dictionary of numbers and their squares.
l = {i : i*i for i in range (1,11)}
print(l)

# Q22. WAP to create a dictionary of even numbers and their cubes.
l = {i : i**3 for i in range (1,11) if i %2 ==0}
print(l)

# Q23. WAP to create a dictionary of characters and their ASCII values.
l = {i : ord(i) for i in 'ABCHS'}
print(l)

# Q24. WAP to create a dictionary of names and their lengths.
l = {i : len(i) for i in ('Nikky','Baby','Sai')}
print(l)

# Syntax 2 : {key:value for var1,var2 in zip(col1,col2)}

# Q25. WAP to create a dictionary of student names and marks.
names = ['Nikky', 'Sai', 'Ajay']
marks = [85, 72, 91]

l = {i:j for i,j in zip(names, marks)}
print(l)

# Q26. WAP to create a dictionary of product names and prices.
products = ['Pen', 'Book', 'Bag']
prices = [20, 50, 500]

l = {i:j for i,j in zip(products, prices)}
print(l)

# Q27. WAP to create a dictionary of employee names and salaries.
names = ['Nikky', 'Rahul', 'Anitha']
salary = [25000, 30000, 28000]

l = {i:j for i,j in zip(names, salary)}
print(l)

# Syntax 3 : {key:value1 if condition else value2 for var1,var2 in zip(col1,col2)}

# Q28. WAP to create a dictionary of students with "Pass" or "Fail".
names = ['Nikky', 'Sai', 'Ajay']
marks = [80, 25, 65]

l = {i:'Pass' if j >= 35 else 'Fail' for i,j in zip(names, marks)}
print(l)

# Q29. WAP to create a dictionary of employees with "High" or "Low" salary.
names = ['Nikky', 'Rahul', 'Anitha']
salary = [25000, 60000, 45000]

l = {i:'High' if j >= 50000 else 'Low' for i,j in zip(names, salary)}
print(l)

# Q30. WAP to create a dictionary of products with "Available" or "Out of Stock" based on quantity.
products = ['Pen', 'Book', 'Bag']
quantity = [10, 0, 5]

l = {i:'Available' if j > 0 else 'Out of Stock' for i,j in zip(products, quantity)}
print(l)